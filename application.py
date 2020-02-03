from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    a=1
    b=2
    return (a+b)
@app.route("/z")
def hello():
    return "zzzz"
