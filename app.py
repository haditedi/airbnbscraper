import json
from flask import Flask, jsonify, request
from flask_cors import CORS

from main import getBnb

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["post","get"])
def home():
    # data = json.loads(request.data)
    # print(data)
    try:
        getBnb("sky")
    except Exception as e:
        print(e)
    return jsonify("hello world")

if __name__ == '__main__':
   app.run(port=5000)