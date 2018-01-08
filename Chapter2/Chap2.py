
import pandas as pd

rd = pd.read_csv("/Users/shuvamoymondal/Downloads/salesdata.csv")
## to get all the list of method in a series and Dataframe
s_attr_methods = set(dir(pd.Series))
df_attr_methods = set(dir(pd.DataFrame))
print(s_attr_methods)
print(df_attr_methods)
print(rd.columns)

print("_________________________________________________________")
print("To check the count of a dataframe or relative frequency, Need to use value_counts()")
city = rd.city
print("to get the relative frequency of City" ,city.value_counts(normalize=True).head(4))
print("Count of City" ,city.value_counts().head(4))

print("_________________________________________________________")
print("To check the size of a dataframe column, Need to use size,len,shape method")
city = rd.city
print("Count of City" ,city.size ,len(city) , city.shape)

print("_________________________________________________________")
print("To check the count of non missing value of a dataframe column, Need to use count()")
print("Count of non missing value of City" ,city.count())

print("_________________________________________________________")
print("To use group method, standard devation in dataframe")
round_col = rd.raisedAmt
print("group function output" ,round_col.mean(),round_col.min(),round_col.max(),round_col.std(),round_col.median())

print("_________________________________________________________")
print("If you want to see summary of statistics of the quantile function")
print("Summary statistics:" , round_col.describe())

print("_________________________________________________________")
print("If you want to see the division of value using quantile function")
print("To see quantile" ,round_col.quantile([.1,.2,.3,.4,.5,.6,.7,.8,.9]).head(20))

print("_________________________________________________________")
print("If you want to see the null value check")
print("Null value check {}".format(city.isnull().head(4)))

print("_________________________________________________________")
print("If you want to see the notnull value check")
print("Null value check {}".format(city.notnull().head(4)))
print("Null value check with hasnans{} ".format(city.hasnans))

print("_________________________________________________________")
print("Null value replce with fillna")
print(city.fillna(0).head(4))








