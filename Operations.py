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
        rep = op.calculateTotals(date, rep);
        return rep;

    def loadData(self):
        today = datetime.datetime.utcnow();
        if (Data.loadTime is None):
            Data.load();
        elif ((today - Data.loadTime).days > 0):
            Data.load();
    
    def calculateTotals(self, date, rep):
        op = Operations();
        dt = datetime.datetime.strptime(date,"%Y-%m-%d");
        nextdt = dt + datetime.timedelta(days=1);
        Data.orders['created_at'] = pd.to_datetime(Data.orders['created_at'],format="%Y-%m-%d %H:%M:%S.%f")
        resp = Data.orders[(Data.orders['created_at'] >= dt) & (Data.orders['created_at'] < nextdt)];
        customer = resp.drop_duplicates(subset="customer_id");
        order_lines = pd.merge(resp, Data.order_lines, left_on="id",right_on="order_id");
        rep.items = order_lines['quantity'].sum();
        rep.customers = len(customer['customer_id']);
        rep.total_discount_amount = order_lines['discounted_amount'].sum();
        rep.discount_rate_avg = order_lines['discount_rate'].sum() / len(order_lines['discount_rate']);
        rep.order_total_avg = order_lines['total_amount'].sum() / len(order_lines['total_amount']);
        return rep;
