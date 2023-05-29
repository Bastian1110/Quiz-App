from flask import Flask, request, jsonify
from flask_cors import CORS
from quiz_app import MongoManager, User

app = Flask("Quiz App Server")
CORS(app)

my_manager = MongoManager("mongodb://localhost:27017", "quizapp")
my_user = User(my_manager)


@app.route("/")
def ping():
    return jsonify({"message": "Hello from QuizApp"}), 200


@app.route("/register", methods=["POST"])
def register():
    username = request.values.get("username")
    password = request.values.get("password")
    if not username or not password:
        return jsonify({"message": "Missing values"}), 400
    try:
        message, result = my_user.create_user(username, password)
        if result == 0:
            return jsonify({"message": message}), 200
        return jsonify({"message": message}), 400
    except Exception as e:
        print(e)
        return jsonify({"message": "Error creating the user"}), 500


@app.route("/login", methods=["POST"])
def login():
    username = request.values.get("username")
    password = request.values.get("password")
    if not username or not password:
        return jsonify({"message": "Missing values"}), 400
    try:
        message, result, token = my_user.validate_user(username, password)
        if result == 0:
            return jsonify({"message": message, "token": token}), 200
        return jsonify({"message": message}), 400
    except Exception as e:
        print(e)
        return jsonify({"message": "Error validating the user"}), 500


@app.route("/updateScore", methods=["POST"])
def handleScore():
    score = request.values.get("score")
    token = request.values.get("token")
    if not score or not token:
        return jsonify({"message": "Missing values"}), 400
    try:
        message, result, new_score = my_user.update_score(token, score)
        if result == 0:
            return jsonify({"message": message, "new_score": new_score}), 200
        return jsonify({"message": message}), 400
    except:
        return jsonify({"message": "Error updating score"}), 500


if __name__ == "__main__":
    app.run(port=8080, debug=True)
