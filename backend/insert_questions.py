import json
from pymongo import MongoClient

# Establish connection to MongoDB server
client = MongoClient("mongodb://localhost:27017/")

# Access the database and collection
db = client["quizapp"]
collection = db["question"]

# Load JSON data
with open("questions.json") as file:
    data = json.load(file)

# Insert each object into the collection
for obj in data:
    collection.insert_one(obj)

# Close the connection
client.close()
