# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 14:38:58 2020

@author: ragur
"""

#import the car_price dataset

import pandas as pd 


car_price = pd.read_csv("C:/Users/ragur/Downloads/CarPrice_Assignment.csv")

# knowing the details of the data set
def details(car_price):
    print(car_price.describe())
    print(car_price.info())

details(car_price)

# finding the missing values
class missing_values:
    def __init__(self,data):
        self.data = data
    def find_missed(self):
        return self.data.isnull().sum()
missed = missing_values(car_price) 
number_of_missed = missed.find_missed()
print(number_of_missed)

# finding categorical values of features
print(car_price.dtypes)
# here CarName,fueltype,aspiration,doornumber,carbody,drivewheel,enginelocation,enginetype,cylindernumber and fuel system are in the object data type

def add_dummies(data):
    return pd.get_dummies(data,columns=["CarName","fueltype","aspiration","doornumber","carbody","drivewheel","enginetype","enginelocation","cylindernumber","fuelsystem"])
well_struct_data = add_dummies(car_price)
print(well_struct_data)  



