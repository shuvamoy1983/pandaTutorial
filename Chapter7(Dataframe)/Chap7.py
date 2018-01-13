import pandas as pd
import numpy as np

rd = pd.read_csv("/Users/shuvamoymondal/Downloads/cookbook/data/employee.csv")

##Create an Empty DataFrame
v = pd.DataFrame()
print(v)

##Create a DataFrame from Lists
p = [1,2,3,4]
v =pd.DataFrame(p, index=[10,20,30,40])
print(v)

data = [['Alex',10],['Bob',20],['Marshal',30]]
v= pd.DataFrame(data)
print(v)

##Create a DataFrame from Dict of ndarrays / Lists
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
v= pd.DataFrame(data)
print(v)

##Let us now create an indexed DataFrame using arrays.

data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
v= pd.DataFrame(data,index=[10,20,30,40])
print(v)

##Create a DataFrame from List of Dicts
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
v= pd.DataFrame(data,index=['first','second'],columns=['a','b','c1'])
print(v)

