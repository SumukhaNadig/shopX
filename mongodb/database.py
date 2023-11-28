from fastapi.encoders import jsonable_encoder
from motor.core import AgnosticDatabase
from motor.motor_asyncio import AsyncIOMotorClient
from models.order_model import Order
import certifi

import config
from models.user_model import Customer
ca = certifi.where()


def db_connection():
    client = AsyncIOMotorClient(config.MONGODB_CONNECTION_URL, tlsCAFile=ca)
    db = client[config.MONGODB_DATABASE_NAME]
    return db

async def find_document(collection_name: str, query: dict, multiple: bool= False) ->dict|None:
    try:
        if multiple:
            document = await db[collection_name].find(query).to_list(1000)
        else:
            document = await db[collection_name].find_one(query)
        return document
    except Exception as e:
        return {e}


# update operation
async def update_one(collection_name: str, filter_query: dict, updated_data: dict):
    try:
        document = await db[collection_name].update_one(
            filter=filter_query, update=updated_data, upsert=True
        )
        return document
    except Exception as e:
        return {}

async def insert_one(collection_name: str, new_data: Order| Customer):
    try:
        document = await db[collection_name].insert_one(
            document=jsonable_encoder(new_data),
        )
        return document
    except Exception as e:
        return {}


db: AgnosticDatabase = db_connection()
