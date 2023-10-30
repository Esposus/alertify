from datetime import datetime

from fastapi import APIRouter, HTTPException, Query, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from database import notifications_collection
from schemas import (
    Notification, ReadNotificationParams
)
from send_email import send_email


router = APIRouter()


@router.post("/create", response_model=dict)
async def create_notification(notification: Notification):
    try:
        notification_id = str(datetime.utcnow().timestamp())
        notification_dict = notification.model_dump()  # .dict() заменил на .model_dump()  # noqa
        notification_dict.update(
            {
                "id": notification_id,
                "timestamp": datetime.utcnow().timestamp(),
                "is_new": True,
            }
        )
        notifications_collection.update_one(
            {"user_id": notification.user_id},
            {"$push": {"notifications": notification_dict}},
            upsert=True
        )

        if notification.key == "registration" or notification.key == "new_login":
            send_email(notification.key)
        return JSONResponse(content=jsonable_encoder(
            {"success": True}), status_code=status.HTTP_201_CREATED
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'Внутренняя ошибка сервера: {str(e)}'
        )


@router.get("/list", response_model=dict)
async def list_notifications(
    user_id: str,
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1)
):
    try:
        user_notifications = await notifications_collection.find_one(
            {"user_id": user_id}, {"_id": 0, "notifications": 1}
        )
        if not user_notifications or not user_notifications.get("notifications"):
            return JSONResponse(
                content=jsonable_encoder(
                    {"success": True, "data": {"elements": 0, "new": 0, "list": []}}
                )
            )
        notifications = user_notifications["notifications"]
        total_elements = len(notifications)
        new_elements = sum(1 for notification in notifications if notification["is_new"])
        response_data = {
            "elements": total_elements,
            "new": new_elements,
            "request": {"user_id": user_id, "skip": skip, "limit": limit},
            "list": notifications[skip:skip + limit]
        }
        return JSONResponse(content=jsonable_encoder({"success": True, "data": response_data}))
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'Внутренняя ошибка сервера: {str(e)}'
        )


@router.post("/read")
async def read_notification(params: ReadNotificationParams) -> JSONResponse:
    try:
        user_id = params.user_id
        notification_id = params.notification_id
        result = await notifications_collection.update_one(
            {"user_id": user_id, "notifications.id": notification_id},
            {"$set": {"notifications.$.is_new": False}}
        )
        if result.matched_count == 0:
            return JSONResponse(
                content=jsonable_encoder(
                    {"success": False, "message": "Сейчас уведомлений нет"}
                ),
                status_code=status.HTTP_404_NOT_FOUND
            )
        return JSONResponse(content=jsonable_encoder({"success": True}))
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'Внутренняя ошибка сервера: {str(e)}'
        )
