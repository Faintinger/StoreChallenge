import flask;
import json;
import datetime;
import Operations;
import sys, traceback
from flask import request, jsonify;

app = flask.Flask(__name__);

@app.route('/HelloWorld')
def helloworld():
    return {"Response": "Hello, World!"};


@app.route('/ReloadData')
def reloadData():
    Operations.Operations().loadData();
    return {"Response": "Data Reload!"};


@app.route('/DateReport', methods=['GET'])
def report():
    date = request.args.get('date');
    try:
        dt = datetime.datetime.strptime(date,"%Y-%m-%d");
        result = Operations.Operations.generateReport(date);
        return json.dumps(result.__dict__);
    except Exception as e:
        traceback.print_exc();
        print(e);
        return {'error' : 'This is not a valid date format'};


if __name__ == '__main__':
    app.run(debug = True, port=8080)