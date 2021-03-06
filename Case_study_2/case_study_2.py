# -*- coding: utf-8 -*-
"""Case_Study_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jg-iyYHMPjI_XMQOW-Q5LdsNlUan1Mxh
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('casestudy.csv')

df.head()

df.drop('Unnamed: 0', axis=1, inplace=True)
le = LabelEncoder()
df['customer_email'] = le.fit_transform(df['customer_email'])

df.head()

df.customer_email.value_counts()

df.info()

df.describe()

df15 = df[df.year == 2015]
df16 = df[df.year == 2016]
df17 = df[df.year == 2017]

total_revenue = df.groupby('year')['net_revenue'].sum()
print(total_revenue)
print('*'*80)
print('\n')

new_cust16 = df16[~df16.customer_email.isin(df15.customer_email)]
new_cust17 = df17[~df17.customer_email.isin(df16.customer_email)]
print('New customer revenue for year 2016: ', round(new_cust16['net_revenue'].sum(),2))
print('New customer revenue for year 2017: ', round(new_cust17['net_revenue'].sum(),2))
print('*'*80)
print('\n')

exist_cust16 = df16[df16.customer_email.isin(df15.customer_email)]
exist_cust16prev = df15[df15.customer_email.isin(df16.customer_email)]
exist_cust17 = df17[df17.customer_email.isin(df16.customer_email)]
exist_cust17prev = df16[df16.customer_email.isin(df17.customer_email)]
print('Existing customer growth for year 15-16: ', round(exist_cust16['net_revenue'].sum()-exist_cust16prev['net_revenue'].sum(),2))
print('Existing customer growth for year 16-17: ', round(exist_cust17['net_revenue'].sum()-exist_cust17prev['net_revenue'].sum(),2))
print('*'*80)
print('\n')

attr_cust15 = df15[~df15.customer_email.isin(df16.customer_email)]
attr_cust16 = df16[~df16.customer_email.isin(df17.customer_email)]
print('Revenue lost in 2016 due to attrition from year 2015: ',round(attr_cust15['net_revenue'].sum(),2))
print('Revenue lost in 2017 due to attrition from year 2016: ',round(attr_cust16['net_revenue'].sum(),2))
print('*'*80)
print('\n')

print('Existing customer revenue Current Year for 2016: ', round(exist_cust16['net_revenue'].sum(),2))
print('Existing customer revenue Prior Year for 2016: ', round(exist_cust16prev['net_revenue'].sum(),2))
print('Existing customer revenue Current Year for 2017: ', round(exist_cust17['net_revenue'].sum(),2))
print('Existing customer revenue Prior Year for 2017: ', round(exist_cust17prev['net_revenue'].sum(),2))
print('*'*80)
print('\n')

print('Total customers for the year 2015: ', len(df15.customer_email.unique()))
print('Total customers for the year 2016: ', len(df16.customer_email.unique()))
print('Total customers for the year 2017: ', len(df17.customer_email.unique()))
print('*'*80)
print('\n')

print('Total customers Previous Year for 2015: -')
print('Total customers Previous Year for 2016: ', len(df15.customer_email.unique()))
print('Total customers Previous Year for 2017: ', len(df16.customer_email.unique()))
print('*'*80)
print('\n')

print('New customers for year 2016: ', len(new_cust16.customer_email.unique()))
print('New customers for year 2017: ', len(new_cust17.customer_email.unique()))
print('*'*80)
print('\n')

print('Lost customers for year 2016: ', len(attr_cust15.customer_email.unique()))
print('Lost customers for year 2017: ', len(attr_cust16.customer_email.unique()))
print('*'*80)
print('\n')

plt.figure(figsize=(20,10))
sns.histplot(data=df, x='net_revenue',bins=125, hue='year')
plt.xlabel('Amount spent')
plt.show()

plt.figure(figsize=(20,10))
sns.boxplot(x='year',y='net_revenue',data=df)
plt.show()

plt.figure(figsize=(20,10))
sns.scatterplot(data=df, x='customer_email', y='net_revenue', hue='year')
plt.legend(loc='upper right')
plt.xlabel('CustomerID')
plt.show()