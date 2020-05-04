import json;
import datetime;
import pandas as pd;
from Data import Data;
from Objects.Report import Report;
from Objects.Commission import Commission;

class Operations(object):
    """
        Class Operation
            Class Dedicated to process all the information for the response
    """

    @staticmethod
    def generateReport(date):
        op = Operations();
        op.loadData();
        rep = Report();
        return rep;

    def loadData(self):
        today = datetime.datetime.utcnow();
        if (Data.loadTime is None):
            Data.load();
        elif ((today - Data.loadTime).days > 0):
            Data.load();
    

    def calculateTotals(self, date, rep):
        return rep;
