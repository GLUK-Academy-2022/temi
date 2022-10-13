from flask import *
import json, time

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home_page():
    data_set = {
        "Page": "Home",
        "Message": "Successfully loaded home page",
        "Timestamp": time.time(),
    }
    json_dump = json.dumps(data_set)

    return json_dump


@app.route("/hello", method=["GET"])
def hello():

    return "teamname"


if __name__ == "__main__":
    app.run(debug=True, port=8000)
