from pymongo import MongoClient
from random import randint
from hashlib import sha256
from jwt import encode, decode


class MongoManager:
    def __init__(self, mongo_uri: str, database_name):
        self.db_client = MongoClient(mongo_uri)[database_name]


class User:
    def __init__(self, db_manager):
        self.collection = db_manager.db_client["user"]

    def create_user(self, username: str, password: str):
        documents = self.collection.find({"username": username})
        for document in documents:
            if document:
                return ["User already exists", 1]
        user = {
            "username": username,
            "password": sha256(password.encode("utf-8")).hexdigest(),
            "score": 0,
            "avatar": randint(0, 100),
        }
        result = self.collection.insert_one(user)
        return ["User created!", 0]

    def validate_user(self, username: str, password: str):
        password = sha256(password.encode("utf-8")).hexdigest()
        documents = self.collection.find({"username": username, "password": password})
        for document in documents:
            if document:
                document["_id"] = str(document["_id"])
                document.pop("password")
                return [
                    "Success",
                    0,
                    encode({"user": document}, "Chikimiau"),
                ]
        return ["Bad username or password", 1, None]

    def update_score(self, token, score):
        data = decode(token, "Chikimiau", algorithms=["HS256"])["user"]
        try:
            print(data["_id"])
            result = self.collection.find({"_id": data["_id"]})
            for i in result:
                print("miau", i)
            return ["Success", 0, score]
        except Exception as e:
            print("here ", e)
            return ["Bad token", 1, None]
