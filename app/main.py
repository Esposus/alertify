from fastapi import FastAPI

from config import settings
from routers import router as api_router

app = FastAPI(title=settings.app_title, description=settings.description)
app.include_router(api_router)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', reload=True)
