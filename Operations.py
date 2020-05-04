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
        rep = op.toString(rep);
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
        if len(order_lines['discount_rate']) > 0:
            rep.discount_rate_avg = order_lines['discount_rate'].sum() / len(order_lines['discount_rate']);
            rep.order_total_avg = order_lines['total_amount'].sum() / len(order_lines['total_amount']);
        else:
            rep.discount_rate_avg = 0;
            rep.order_total_avg = 0;
        comm = op.calculateCommissions(order_lines, date);
        rep.commissions = comm;
        return rep;

    def calculateCommissions(self, df, date):
        total = 0;
        comm = Commission();
        promotions = dict();
        vendor = Data.vendor_commissions[Data.vendor_commissions.date == date];
        vendor_order = pd.merge(df,vendor,left_on='vendor_id',right_on='vendor_id');
        product_promotions = pd.merge(Data.promotions, Data.product_promotions, left_on='id',right_on='promotion_id');
        product_promotions = product_promotions[product_promotions.date == date];
        for row in range(len(Data.promotions)):
            prom = Data.promotions.loc[row, 'description'];
            tmp = product_promotions[product_promotions.description == prom];
            tmp = pd.merge(tmp, vendor_order,left_on='product_id',right_on='product_id')
            promotions[prom] = (tmp.total_amount * tmp.rate).sum();
            total = total + promotions[prom];
        comm.promotions = promotions;
        comm.total = total;
        comm.order_average = 0 if len(vendor_order['order_id'])== 0 else total / len(vendor_order['order_id']);
        return comm;


    def toString(self, rep):
        rep.customers = int(rep.customers);
        rep.items = int(rep.items);
        rep.total_discount_amount = float(rep.total_discount_amount);
        rep.order_total_avg = float(rep.order_total_avg);
        rep.discount_rate_avg = float(rep.discount_rate_avg);
        rep.commissions.total = float(rep.commissions.total);
        rep.commissions.order_average = float(rep.commissions.order_average);
        for v in rep.commissions.promotions:
            rep.commissions.promotions[v] = float(rep.commissions.promotions[v]);
        rep.commissions = json.dumps(rep.commissions.__dict__);
        return rep;