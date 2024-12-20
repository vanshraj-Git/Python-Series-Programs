import pandas as pd 
import numpy as np

dict1={
    'name':['Vanshraj','Hitanshu','Jay','Yashan'],
    'RollNo.':[1,2,3,4],
    'Place':['Odhav','Bapunagar','Hatkashwar','Maninagar']
}
df=pd.DataFrame(dict1)  #created dictionary into table form 
print(df)

print(df.head(2)) #First 2 rows.
print(df.tail(2)) #Last 2 rows.
print(df.describe())
df.to_csv('schoolfriendsindexfalse.csv')
df.to_csv('schoolfriendsindexfalse.csv',index=False) #Code to excel (csv) without index 0,1,2,3.


