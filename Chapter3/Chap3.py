import pandas as pd

##Choose a col as index columns
rd = pd.read_csv("/Users/shuvamoymondal/Downloads/salesdata.csv",index_col='fundedDate')
#print(rd.head(3))


print("_________________________________________________________")
print("Renaming value of a row of index column and other column rename")
##Renaming value of a row of index column and other column rename
##you can not rename index column
Row_rename ={'1-May-07':'2007-05-01'}
col_rename = {'permalink': 'PermaLink','city': 'CITY'}
rd_rnm = rd.rename(index=Row_rename,columns=col_rename)
#print(rd_rnm.head(2))

print("_________________________________________________________")
print("There is other way to change the column name and row value after converting to to_list")
## There is other way to change the column name and row value after converting to to_list
actual_indx= rd.index
actual_col= rd.columns
print(actual_indx)
print(actual_col)
indx =rd.index.tolist()
cols= rd.columns.tolist()
indx[0] = '2-May-09'
indx[1] = '2-OCT-09'
cols[3] ='CATG'
cols[0] ='PERMALINK'

actual_indx=indx
actual_col=cols
print(actual_col)
print(actual_indx)

###Creating and deleting Columns
print("_________________________________________________________")
print("Creating and deleting Columns")
rd['actor_detail'] = (
         rd['company'] +
         rd['category'])

print("_________________________________________________________")
print("Fill value where null value found and checking at the end if there is any null with sum()")
rd['actor_detail']= rd['actor_detail'].fillna(0)
print(rd['actor_detail'].isnull().sum())
print(rd.columns)

## you can delete the column using del operator
print("_________________________________________________________")
print("Deleting column")
del rd['actor_detail']
print(rd.columns)

