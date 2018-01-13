import pandas as pd
import numpy as np

rd = pd.read_csv("/Users/shuvamoymondal/Downloads/salesdata.csv")
##print(rd.columns)
print(rd.shape)
## this is for max and min check for individual columns
print(rd['raisedAmt'].min())
## this is for max and min check for all columns.
print(rd.min() + rd.max())
## this is for checking missing values.
print(rd.min(skipna=False))

##determine whether there are any missing values in the DataFrame use any”
print(rd['numEmps'].isnull().any())



