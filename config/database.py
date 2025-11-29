from pymongo import MongoClient

MONGO_URI = "mongodb://localhost:27017/bookDB"

client = MongoClient(MONGO_URI)

db = client["todo_db"]

collection_name = db["todo_collection"]
