import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

import config


client = AsyncIOMotorClient(config.settings.DB_URI)
db = client["alertify"]
notifications_collection = db["notifications"]


async def main():
    data = notifications_collection.find({})
    print(data)


asyncio.run(main())
