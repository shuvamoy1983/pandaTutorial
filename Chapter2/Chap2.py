
import pandas as pd

rd = pd.read_csv("/Users/shuvamoymondal/Downloads/salesdata.csv")
## to get all the list of method in a series and Dataframe
s_attr_methods = set(dir(pd.Series))
df_attr_methods = set(dir(pd.DataFrame))
print(s_attr_methods)
print(df_attr_methods)
print(rd.columns)

print("_________________________________________________________")
print("To check the count of a dataframe, Need to use value_counts()")
city = rd.city
print("Count of City" ,city.value_counts())

