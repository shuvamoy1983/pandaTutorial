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

##Column Addition on Dataframe

d = {'one' :pd.Series([10,20,30],index=[1,2,3]),
     'two' :pd.Series([20,30,30,40],index=[1,2,3,4])
    }

v= pd.DataFrame(d)
v['three'] =pd.Series([10,20,30],index=[1,2,3])
print(v)

v['four'] = v['one'] + v['two']
print(v)

##column deletion
del v['three']
print(v)

##Row Selection, Addition, and Deletion

print("Selection by Label(means entire row")
print(v.loc[2])

###Selection by integer location
print("_______________")
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
     'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print(df.iloc[2])

##Slice Rows
print("Multiple rows can be selected using ‘ : ’ operator.")
print(df[2:4])

###Addition of Rows
print("Addition of Rows using apend")
df1 = df.append(v)
print(df1)

##Deletion of Rows
print("Deletion of rows using index value")
print(df1.drop('a'))