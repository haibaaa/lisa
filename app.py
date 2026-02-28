from flask import Flask

app = Flask(__name__)


@app.route("/")
def hi():
    return {
        "yooo": "nyurururur nega what's good",
    }
