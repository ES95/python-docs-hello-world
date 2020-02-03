from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/")
def hello():
    text = str(request.args.get('text'))
    return text
