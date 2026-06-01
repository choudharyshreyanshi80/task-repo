#	Create a Pandas Series  

import pandas as pd

dic={"name":"Shree","branch":"DS","cgpa":9.3}
ser1=pd.Series(dic)
print("Series from Dictionary:")
print(ser1)

marks=[93,91,93,89,87]
ser2=pd.Series(marks)
print("\nSeries from List:")
print(ser2)

print("\nAccessing Elements:")
print(ser1.iloc[0])
print(ser2[:2])

#Pandas DataFrame 

lst=[[1,2,3],[4,5,6],[7,8,9]]
df1=pd.DataFrame(lst)
print("\nDataFrame from Two-Dimensional List:")
print(df1)

dic={"name":"Shree","branch":"DS","cgpa":9.3}
df2=pd.DataFrame(dic,index=[0])
print("\nDataFrame from Dictionary:")
print(df2)

lst1=[
     [1, "DS", 9.3],
    [2, "CS", 8.9],
    [3, "IT", 8.7]]
df3=pd.DataFrame(lst1)
print("\nDataFrame from List of Lists:")
print(df3)

tup=[("sub1",99),("sub2",95),("sub3",93)]
df4=pd.DataFrame(tup)
print("\nDataFrame from List of Tuples:")
print(df4)

dicts= [
    {"Name": "Shree", "Age": 20},
    {"Name": "Riya", "Age": 21},
    {"Name": "Aman", "Age": 22}
]
df5 = pd.DataFrame(dicts)
print("\nDataFrame from List of Dictionaries:")
print(df5)

# Data iteration
data={
    "Name": ["Shree", "Riya", "Neha"],
    "Age": [20, 21, 22],
    "Marks": [93, 88, 95]
}
df=pd.DataFrame(data)
print(df)
print("\nIterating over rows:")
for index, row in df.iterrows():
    print(index, row["Name"], row["Marks"])

print("\nStudents with Age > 93:")
print(df[df["Marks"] > 93])

print("\nRow:")
print(df.iloc[0])

print("\nFirst Two Rows of Name and Marks:")
print(df.loc[:1, ["Name", "Marks"]])

df_drop = df[df["Marks"] >= 90]
print(df_drop)

df.loc[len(df)] = ["Laksh",22, 95]
print(df)

rows_list = df.values.tolist()
print("\nList from DataFrame Rows:")
print(rows_list)





