import pandas as pd
import numpy as np
from pandas import Series
#Series are objects that have indexes similar to numpy array but are immutable
object = Series([10,15,20,13,14])
print(object)
# Accessing objects in a Series 
print(object.values)
print(object.index)

data = np.array(['a','b','c','d'])
s= Series(data)
print(s)

#modifying indexes
s= Series(data, index =[10,11,12,13])
print('modified indexes are', s.index)

#Using real life data
revenue = Series([20,35,45,56,45,67], index = ['ola','uber','bolt','opay','maxride','seqhub'])
print(revenue [revenue >= 30]) # selecting data from a Series 

#Using Boolean Opeartors
print('lyft' in revenue)

#converting to a dictionary

rev_dict = revenue.to_dict()
print(rev_dict) # keyvalue pair

#Working with null values nan
index2= ['ola','uber','bolt','opay','maxride','seqhub','ocar']
revenue2 = np.append(revenue,[34])
revenue2 = Series(revenue2,index2)
print(revenue2)

#searching for null values
print(pd.isnull(revenue2))

#searching for null values
print(pd.notnull(revenue2))