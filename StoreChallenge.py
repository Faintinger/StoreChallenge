import flask;
import json;
import datetime;
import Operations;
import sys, traceback
from flask import request, jsonify;

app = flask.Flask(__name__);

# HelloWorld Function
# Test of Functionality
# Return Hello World
@app.route('/HelloWorld')
def helloworld():
    return {"Response": "Hello, World!"};

# ReloadData Function
# Triggers the reload of the files to Memory
# Returns a confirmation msg
@app.route('/ReloadData')
def reloadData():
    Operations.Operations().loadData();
    return {"Response": "Data Reload!"};

# Report Function
# Generate the report and retrieve the object
# Return Report object Json serealize
@app.route('/DateReport', methods=['GET'])
def report():
    #receive date in string format yyyy-mm-dd
    date = request.args.get('date');
    try:
        dt = datetime.datetime.strptime(date,"%Y-%m-%d");
        result = Operations.Operations.generateReport(date);
        return json.dumps(result.__dict__);
    except Exception as e:
        #Stack trace and error on console
        traceback.print_exc();
        print(e);
        #Exception trigger by the failure of the datatype convertion
        return {'error' : 'This is not a valid date format'};


if __name__ == '__main__':
    app.run(debug = True, port=8080)