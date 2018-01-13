import pandas as pd
import re
import numpy as np

##Choose a col as index columns
rd = pd.read_csv("/Users/shuvamoymondal/Downloads/salesdata.csv")
print(rd.columns)

print("_________________________________________________________")
print("Selecting Multiple columns with double brackets")
print(rd[['company','raisedAmt']])

print("_________________________________________________________")
print("Selecting columns with methods.select_dtypes used to select int,float columns")
print(rd.get_dtype_counts())
print(rd.select_dtypes(include=['float64']).head(10))

print("_________________________________________________________")
print("Selecting Columns with filter methods for searching column value ")
print(rd.filter(like='raisedAmt').head(3))

print("_________________________________________________________")
print("Selecting multiple Columns with filter and items ")
print(rd.filter(items=['raisedAmt','state']).head(3))

###Example2
mv = pd.read_csv("/Users/shuvamoymondal/Downloads/cookbook/data/movie.csv",index_col='movie_title')
print(mv.columns)
print(mv.get_dtype_counts())
##If I want to see the integer columns only
print(mv.select_dtypes(include=['number']).head(10))
##If I want to see columns contains some specific keyword, select those
pd.options.display.max_rows = 8
print(mv.filter(like='facebook_').head(10))

##If I want to see columns containing some digit,use regex and select those
print(mv.filter(regex='\d'))

