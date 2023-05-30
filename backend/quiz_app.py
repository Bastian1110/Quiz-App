from pymongo import MongoClient
from random import randint
from hashlib import sha256
from jwt import encode, decode
from bson import ObjectId
from random import sample


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
                    document["_id"],
                ]
        return ["Bad username or password", 1, None, None]

    def get_top(self):
        result = list(self.collection.find().sort("score", -1).limit(5))
        for doc in result:
            doc["_id"] = str(doc["_id"])
        return result

    def update_score(self, token, score):
        data = decode(token, "Chikimiau", algorithms=["HS256"])["user"]
        try:
            result = self.collection.update_one(
                {"_id": ObjectId(data["_id"])}, {"$inc": {"score": int(score)}}
            )
            print(result.modified_count)
            return ["Success", 0, score]
        except Exception as e:
            print("here ", e)
            return ["Bad token", 1, None]


class Question:
    def __init__(self, db_manager):
        self.collection = db_manager.db_client["question"]

    def create_question(self, category, question, answers, correct_index):
        try:
            self.collection.insert_one(
                {
                    "category": category,
                    "question": question,
                    "answers": answers,
                    "correct": correct_index,
                }
            )
            return ["Success", 0]
        except:
            return ["Error", 1]

    def generate_quiz(self, n_question, catrgory="Random"):
        quiz = []
        if catrgory == "Random":
            all_documents = list(self.collection.find({}, {"_id": 1}))
        else:
            all_documents = list(
                self.collection.find({"category": catrgory}, {"_id": 1})
            )
        all_documents = [str(doc["_id"]) for doc in all_documents]
        shuffled_documents = sample(all_documents, len(all_documents))
        selected_documents = shuffled_documents[:n_question]
        return ["Success", 0, selected_documents]


class Quiz:
    def __init__(self, db_manager):
        self.questions = db_manager.db_client["question"]
        self.user = db_manager.db_client["user"]

    def getQuestion(self, question_id):
        try:
            result = list(
                self.questions.find(
                    {"_id": ObjectId(question_id)},
                    {"question": 1, "answers": 1},
                )
            )[0]
            result["_id"] = str(result["_id"])
            return ["Success", 0, result]
        except:
            return ["Question dosent exist", 1, None]

    def answerQuestion(self, user_id, question_id, answer):
        result = list(
            self.questions.find({"_id": ObjectId(question_id), "correct": answer})
        )
        if result:
            points = 10 + randint(0, 8)
            self.user.update_one(
                {"_id": ObjectId(user_id)}, {"$inc": {"score": points}}
            )
            return ["Respuesta correcta", 0]
        else:
            return ["Respuesta incorrecta", 1]
