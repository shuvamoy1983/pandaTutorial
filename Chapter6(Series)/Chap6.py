import pandas as pd
import numpy as np

##Series is a one-dimensional labeled array capable of holding data of any type (integer, string, float, python objects, etc
##Create a Series from ndarray
v = np.random.rand(4)
print(pd.Series(v))

##Giving index value to Series
print(pd.Series(v,index=[100,101,102,103]))

##Create a Series from dict
data = {'a' : 0., 'b' : 1., 'c' : 2.}
print(pd.Series(data))

##index order can be changed and missing element is filled with NaN
print(pd.Series(data,index=['b','c','d','a']))

##Create a Series from Scalar
s = pd.Series(5, index=[0, 1, 2, 3])
print(s)

##Accessing Data from Series with Position
##Data in the series can be accessed similar to that in an ndarray.
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
print(s[1])

#retrieve the first three element
print(s[:3])
#Retrieve the last three elements
print(s[-3:])
#retrieve a single element
print(s['a'])