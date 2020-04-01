from flask import Flask, render_template, request
import json

import FileReader

with open('/Users/mindyp/PycharmProjects/Webservice/AMZN.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
testJson = data

app = Flask(__name__)

text="123"
@app.route('/')
def index():

    return render_template("testHTML.html", variable=testJson)


# def testGet():
#   if request.method == "GET":
#      return "Hello"


if __name__ == '__main__':
    app.run()
