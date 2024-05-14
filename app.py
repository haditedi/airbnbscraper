import json
from flask import Flask, jsonify, request
from flask_cors import CORS

from utils import getRates
from main import getBnb

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["post","get"])
def home():
    #"Enter 'sky' for Sky Garden or 'hunt' for Hunter House or 'prince' : "
    # getBnb(datalist, arrivalDate, num_days, min_nights)
    if request.data:
        data = json.loads(request.data)
        property_name = data["property"]
        print(data["property"])
        getBnb(property_name, "20-05-2024", "2", "4")
    # try:
    #     getBnb("sky")
    # except Exception as e:
    #     print(e)
    return jsonify(data)

if __name__ == '__main__':
   app.run(debug=True)