import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from .settings import BASE_DIR
from io import StringIO


def month_to_year(x):
    return 2000 + int(x[-2:])


class EDA :
    def __init__(self):
        self.meat_df = pd.read_csv(os.path.join(BASE_DIR, 'eda_proj', 'Meat_prices.csv'))

        self.meat_list = [('Chicken Price', 'Chicken'), ('Beef Price', 'Beef'),
                          ('Lamb Price', 'Lamb'), ('Pork Price', 'Pork'), ('Salmon Price', 'Salmon')]
        self.meat_by_year = self.init_meat()
        self.normal_price = self.normalize_meat()
        self.relative_price = self.relative()

        self.x = range(2000, 2015)

    def init_meat(self):
        self.meat_df = self.meat_df[117:297]
        self.meat_df['Month'] = self.meat_df['Month'].apply(month_to_year)
        self.meat_df.rename(columns = {'Month' : 'Year', 'Lamb price' : 'Lamb Price'}, inplace = True)
        self.meat_df['Pork Price'] = self.meat_df['Pork Price']/100
        return self.meat_df.groupby(['Year']).mean()

    def normalize_meat(self):
        normal_meat = self.meat_by_year.copy()
        for key in self.meat_by_year.keys() :
            key_max = normal_meat[key].max()
            key_min = normal_meat[key].min()
            normal_meat[key] = (normal_meat[key] - key_min) / (key_max - key_min)
        return normal_meat

    def relative(self):
        relative_price = self.normal_price.copy()
        for key in relative_price.keys():
            relative_price[key] = relative_price[key] - (relative_price.index - 2000)/14
        return relative_price

    def plot_meat_year(self):
        plt.figure(figsize = (10, 10))
        for y in self.meat_list:
            plt.plot(self.x, self.meat_by_year[y[0]], label = y[1])
        plt.xlabel('Year')
        plt.ylabel('Price (US dollar)')
        plt.legend()
        fig = plt.figure()
        imgdata = StringIO()
        fig.savefig(imgdata, format = 'svg')
        imgdata.seek(0)
        data = imgdata.getvalue()
        return data
        plt.savefig('plot_meat_price.png')

    def plot_normalized_price(self):
        plt.figure(figsize = (10, 10))
        for y in self.meat_list:
            plt.plot(self.x, self.normal_price[y[0]], label = y[1])
        plt.xlabel('Year')
        plt.ylabel('Normalized Price')
        plt.legend()
        fig = plt.figure()
        imgdata = StringIO()
        fig.savefig(imgdata, format = 'svg')
        imgdata.seek(0)
        data = imgdata.getvalue()
        return data
        plt.savefig('plot_meat_price.png')

    def plot_relative_price(self):
        plt.figure(figsize = (10, 10))
        for y in self.meat_list:
            plt.plot(self.x, self.relative_price[y[0]], label = y[1])
        plt.xlabel('Year')
        plt.ylabel('Relative Price')
        plt.legend()
        fig = plt.figure()
        imgdata = StringIO()
        fig.savefig(imgdata, format = 'svg')
        imgdata.seek(0)
        data = imgdata.getvalue()
        return data

        plt.savefig('plot_meat_price.png')

    def plot_meat(self, price_type):
        print(1)
        if price_type == 'Nothing' :
            return self.plot_meat_year()
        elif price_type == 'Normal' :
            return self.plot_normalized_price()
        else :
            return self.plot_relative_price()

    def bar_plot_meat(self, year):
        x = 3
