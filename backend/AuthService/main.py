from flask import Flask, request, jsonify
from flask_cors import CORS
from os import environ

app = Flask("Quiz App Auth Service")
CORS(app)


@app.route("/test", methods=["GET"])
def test():
    return jsonify({"message": "All ok"}), 200


if __name__ == "__main__":
    app.run(port=environ.get("PORT"))
