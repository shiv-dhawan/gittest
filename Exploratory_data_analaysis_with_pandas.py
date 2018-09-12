# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pandas as pd
# we don't like warnings
# you can comment the following 2 lines if you'd like to
import warnings
warnings.filterwarnings('ignore')

#reading the data
df = pd.read_csv('telecom_churn.csv')
df.head()

#Let’s have a look at data dimensionality, features names, and feature types.

print(df.shape)

#printing out the names of the columns or features
print(df.columns)

#output some general information about the dataframe
print(df.info())

#change the column type Churn  feature to convert it into int64
df['Churn'] = df['Churn'].astype('int64')

'''The describe method shows basic statistical characteristics of each numerical feature 
(int64 and float64 types): number of non-missing values, mean, standard deviation, 
range, median, 0.25 and 0.75 quartiles'''

df.describe()

'''In order to see statistics on non-numerical features,
one has to explicitly indicate data types of interest in the include parameter.'''

df.describe(include=['object', 'bool'])

df['Churn'].value_counts()

'''This shows 2850 users out of 3333 are loyal; their Churn value is 0.
 To calculate the proportion, pass normalize=True to the value_counts function'''
 
 df['Churn'].value_counts(normalize=True)
 
'''A DataFrame can be sorted by the value of one of the variables (i.e columns).
For example, we can sort by Total day charge (use ascending=False to sort in descending order)'''

df.sort_values(by='Total day charge', ascending=False).head()

'''Alternatively to sort by multiple column 
df.sort_values(by=['Churn', 'Total day charge'], ascending=[True, False]).head()'''

#what is the proportion of churned users in our dataframe?
df['Churn'].mean()

#What are average values of numerical variables for churned users?
df[df['Churn'] == 1].mean()

#How much time (on average) do churned users spend on phone during daytime?
df[df['Churn'] == 1]['Total day minutes'].mean()


'''What is the maximum length of international calls among loyal users (Churn == 0) 
who do not have an international plan?'''
 
df[(df['Churn'] == 0) & (df['International plan'] == 'No') ]['Total intl minutes'].max()

'''DataFrames can be indexed by column name (label) or row name (index) or by the serial number 
of a row.The loc method is used for indexing by name, while iloc() is used for indexing by number.'''

df.loc[0:5, 'State':'Area code']

df.iloc[0:5, 0:3]

#If we need the first or last line of the data frame, we can use the df[:1] or df[-1:] construct

df[-1:]

#To apply functions to each column, use apply()
df.apply(np.max)

'''The apply method can also be used to apply a function to each line. 
To do this, specify axis=1. Lambda functions are very convenient in such scenarios. 
For example, if we need to select all states starting with W, we can do it like this:'''

df[df['State'].apply(lambda state: state[0] == 'W')].head()

'''The map method can be used to replace values in a column by passing a dictionary 
of the form {old_value: new_value} as its argument:'''

d = {'No' : False, 'Yes' : True}
df['International plan'] = df['International plan'].map(d)
df.head()


#The same thing can be done with the replace method:
df= df.replace({'Voice mail plan' : d})
df.head()
































































