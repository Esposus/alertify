import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

import config


client = AsyncIOMotorClient(config.settings.db_uri)
db = client["alertify"]
notifications_collection = db["notifications"]


async def main():
    data = await notifications_collection.find_one({})
    print(data)


asyncio.run(main())
