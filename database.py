from pymongo import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient
import certifi
ca = certifi.where()
import os

client = AsyncIOMotorClient(os.environ["MONGODB_URL"], tlsCAFile=ca)

db = client["shopX"]