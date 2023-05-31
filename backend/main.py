from flask import Flask, request, jsonify
from flask_cors import CORS
from quiz_app import MongoManager, User, Question, Quiz

app = Flask("Quiz App Server")
CORS(app)

my_manager = MongoManager("mongodb://localhost:27017", "quizapp")
user_controller = User(my_manager)
question_controller = Question(my_manager)
quiz_controller = Quiz(my_manager)


@app.route("/")
def ping():
    return jsonify({"message": "Hello from QuizApp"}), 200


@app.route("/user/register", methods=["POST"])
def register():
    username = request.values.get("username")
    password = request.values.get("password")
    if not username or not password:
        return jsonify({"message": "Missing values", "result": 1}), 400
    try:
        message, result = user_controller.create_user(username, password)
        if result == 0:
            return jsonify({"message": message, "result": 0}), 200
        return jsonify({"message": message, "result": 1}), 400
    except Exception as e:
        print(e)
        return jsonify({"message": "Error creating the user"}), 500


@app.route("/user/login", methods=["POST"])
def login():
    username = request.values.get("username")
    password = request.values.get("password")
    if not username or not password:
        return jsonify({"message": "Missing values", "result": 1}), 400
    try:
        message, result, token, user_id = user_controller.validate_user(
            username, password
        )
        if result == 0:
            return (
                jsonify(
                    {
                        "message": message,
                        "result": result,
                        "token": token,
                        "user_id": user_id,
                    }
                ),
                200,
            )
        return jsonify({"message": message, "result": result}), 400
    except Exception as e:
        print(e)
        return jsonify({"message": "Error validating the user"}), 500


@app.route("/user/updateScore", methods=["POST"])
def handleScore():
    score = request.values.get("score")
    token = request.values.get("token")
    if not score or not token:
        return jsonify({"message": "Missing values"}), 400
    try:
        message, result, new_score = user_controller.update_score(token, score)
        if result == 0:
            return jsonify({"message": message, "new_score": new_score}), 200
        return jsonify({"message": message}), 400
    except:
        return jsonify({"message": "Error updating score"}), 500


@app.route("/user/getTop", methods=["GET"])
def getTop():
    return jsonify({"message": "Success", "top": user_controller.get_top()})


@app.route("/question/createQuestion", methods=["POST"])
def handleCreateQuestion():
    data = request.get_json()
    try:
        category = data["category"]
        question = data["question"]
        answers = data["answers"]
        correct_index = data["correct_index"]
        message, result = question_controller.create_question(
            category, question, answers, correct_index
        )
        if result == 0:
            return jsonify({"message": message}), 200
        return jsonify({"message": message}), 500
    except:
        return jsonify({"message": "Missing value in the request"}), 400


@app.route("/question/createQuiz", methods=["POST"])
def getQuiz():
    n = int(request.values.get("questions"))
    category = request.values.get("category")
    if not n:
        n = 10
    if not category:
        category = "Random"
    try:
        message, error, questions = question_controller.generate_quiz(n, category)
        return (
            jsonify({"message": message, "questions": questions, "error": error}),
            200,
        )
    except:
        return jsonify({"message": "Error generating quiz", "error": error}), 500


@app.route("/quiz/getQuestion", methods=["POST"])
def handleGetQuestion():
    question_id = request.values.get("id")
    if not question_id:
        return jsonify({"message": "Missing values"}), 400
    message, error, result = quiz_controller.getQuestion(question_id)
    if error == 0:
        return jsonify({"message": message, "question": result}), 200
    return jsonify({"message": message, "question": result}), 400


@app.route("/quiz/answerQuestion", methods=["POST"])
def answer():
    token = request.headers.get("x-access-token")
    if not token:
        return jsonify({"message": "Missing token"}), 400
    question_id = request.values.get("id")
    answer = request.values.get("answer")
    if not answer or not question_id:
        return jsonify({"message": "Missing values"}), 400
    message, result, score = quiz_controller.answerQuestion(
        token, question_id, int(answer)
    )
    return jsonify({"message": message, "result": result, "points": score}), 200


if __name__ == "__main__":
    app.run(port=8080, debug=True)
