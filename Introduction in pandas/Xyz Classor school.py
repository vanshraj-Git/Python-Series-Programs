import pandas as pd 
dict1={
    'Roll No.':[x for x in range(1,101)],
    'Enrollment No.':[x for x in range(22201,22301)],
    'Marks':[x for x in range (1,101)]
}
df=pd.DataFrame(dict1)
# print(df)
print(df.head(3))
print(df.tail(3))
