from flask import Flask
app = Flask(__name__)
# app.debug = True
@app.route("/")
def hello():
   return "Hello"
@app.route("/z")
def helo():
    return "zzzz"
