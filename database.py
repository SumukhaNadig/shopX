from pymongo import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient
import certifi
ca = certifi.where()

uri = "mongodb+srv://abhi:abhi@cluster0.17p1u0e.mongodb.net/?retryWrites=true&w=majority"
client = AsyncIOMotorClient(uri, tlsCAFile=ca)

db = client["shopX"]