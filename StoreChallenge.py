import flask;
import json;
import datetime;
import sys, traceback
from flask import request, jsonify;

app = flask.Flask(__name__);

@app.route('/HelloWorld')
def helloworld():
    return {"Response": "Hello, World!"};


if __name__ == '__main__':
    app.run(debug = True, port=8080)