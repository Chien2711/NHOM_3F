import pandas as pd

class DataCleaner:
    def __init__(self, df):
        self.df = df

    def clean_data(self):
        # Đổi tên cột chuẩn hóa
        self.df.rename(columns={'Invoice': 'InvoiceNo', 'Customer ID': 'CustomerID', 'Price': 'UnitPrice'}, inplace=True)
        self.df['InvoiceNo'] = self.df['InvoiceNo'].astype('str')
        
        # Lọc dữ liệu
        self.df = self.df[~self.df['InvoiceNo'].str.contains('C')]
        self.df = self.df[self.df['Country'] == 'United Kingdom']
        self.df = self.df.dropna(subset=['CustomerID'])
        self.df = self.df[(self.df['Quantity'] > 0) & (self.df['UnitPrice'] > 0)]
        
        return self.df

class BasketPreparer:
    def __init__(self, df):
        self.df = df

    def create_basket(self):
        basket = (self.df.groupby(['InvoiceNo', 'Description'])['Quantity']
                  .sum().unstack().reset_index().fillna(0)
                  .set_index('InvoiceNo'))
        return basket

    def encode_units(self, x):
        if x <= 0: return 0
        if x >= 1: return 1
        return 0