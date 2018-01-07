import pandas as pd
import numpy as np

## How to read data  in panda
rd = pd.read_csv("/Users/shuvamoymondal/Downloads/salesdata.csv")
print(rd.head(2))
print("_________________________________________________________")
## to get index,columns and values
values = rd.values
index = rd.index
col = rd.columns

print("Printing all Col {}".format(col))
print("_________________________________________________________")
print("Printing all values {}".format(values))
print("Printing type for value {}" + format(type(values)))
print("_________________________________________________________")
print("Printing index value {}" + format(index))

print("_________________________________________________________")
print("To check the datatype of all elements")
dt_types = rd.dtypes
print("Dttype {}".format(dt_types))
print("_________________________________________________________")
print("To check the  count of each data type")
dt_count = rd.get_dtype_counts()
print("Dttype {}".format(dt_count))

print("_________________________________________________________")
print("How to select a column in panda")

PermaLink  =rd['permalink'].head(10)
Fund_dt = rd.fundedDate.head(10)
print("Selection of Columns {}".format(PermaLink))
print("Selection of Columns {}".format(Fund_dt))


print("_________________________________________________________")
print("How to convert a column to a panda dataframe")
df = Fund_dt.to_frame()
print("dataframe conversion", df)




