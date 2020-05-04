import os;
import datetime;
import configparser;
import pandas as pd;

class Data(object):
    """
    Class Data
        Store every file as a Pandas Data Frame
        Retrieve files from the location defined in:
            config.properties
    
        Static Class
        Public Access
    """
    config = configparser.RawConfigParser();
    config.read('config.properties');
    loadTime=None;
    orders=None;
    order_lines=None;
    products=None;
    promotions=None;
    product_promotions=None;
    vendor_commissions=None;

    #Load Method
    # Load dataframes from properties file
    @staticmethod
    def load():
        Data.orders = pd.read_csv(Data.config.get('DatabaseSection', 'data.order'));
        Data.order_lines = pd.read_csv(Data.config.get('DatabaseSection', 'data.orderline'));
        Data.products = pd.read_csv(Data.config.get('DatabaseSection', 'data.product'));
        Data.promotions = pd.read_csv(Data.config.get('DatabaseSection', 'data.promotion'));
        Data.product_promotions = pd.read_csv(Data.config.get('DatabaseSection', 'data.productpromotion'));
        Data.vendor_commissions = pd.read_csv(Data.config.get('DatabaseSection', 'data.vendorcommisions'));
        Data.loadTime=datetime.datetime.utcnow();
        