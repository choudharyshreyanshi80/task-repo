# regex patterns

import re
email="shree123@gmail.com"
pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
if re.match(pattern,email):
    print("Valid")
else:
    print("Invalid")


mobile="9765785463"
pattern1=r'^[6-9]\d{9}$'
if re.match(pattern1,mobile):
    print("Valid")
else:
    print("Invalid")


str="user_80"
pattern2=r'^[a-zA-Z0-9_]{4,15}$'
if re.match(pattern2,str):
    print("Valid")
else:
    print("Invalid")


password="User@1234"
pattern3=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=]).{8,}$'
if re.match(pattern3,password):
    print("Strong")
else:
    print("Weak")


# datetime function

import pandas as pd
dates=pd.Series(["2026-06-01","2026-06-02","2026-06-03"])
ser=pd.to_datetime(dates)
print(ser)

print(pd.Timestamp.now())

dates1=pd.date_range(start='2026-06-01',periods=5)
print(dates1)
    
df = pd.DataFrame({
    'Date':['2026-06-01']
})
df['Date'] = pd.to_datetime(df['Date'])
df['Day'] = df['Date'].dt.day_name()
print(df)

start=pd.Timestamp('2026-01-06')
end=pd.Timestamp('2026-01-09')
print(end-start)

# CSV File for Data Analysis

df1=pd.read_csv('emp.csv')
print(df1)
print(df1.head())
print(df1.info())
print(df1.describe())
print(df1.isnull())

df1['Salary']=df1['Salary'].fillna(df1['Salary'].mean())
df1['Experience']=df1['Experience'].fillna(df1['Experience'].median())
print(df1)

df.drop_duplicates(inplace=True)

print(df1.groupby('Department')['Salary'].mean())
print(df1.sort_values(by='Salary',ascending=False))