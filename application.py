from flask import Flask
from flask import request
app = Flask(__name__)

app.config["DEBUG"] = True

@app.route("/")
def hello():
    import requests,json
    text = str(request.args.get('text'))
    main_url = "https://luis-final.cognitiveservices.azure.com/luis/prediction/v3.0/apps/07c0c9aa-7815-4e09-92da-787ab7310d20/slots/staging/predict?subscription-key=3050a2b8146f4ea987465805faa49592&verbose=true&show-all-intents=true&log=true&query="
    url=main_url+text
    response = requests.request('GET',url)
    u=json.loads(response.text)
    return (str(u))

@app.route("/Hello")
def hell():
    return "hello"
