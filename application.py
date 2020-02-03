from flask import Flask
app = Flask(__name__)
app.debug = True
@app.route("/")
def hello():
   retutn "Hello"
@app.route("/z")
def hello():
    return "zzzz"
