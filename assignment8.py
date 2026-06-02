import pandas as pd
# Convert a series of date-strings to a timeseries

ser=pd.Series(["2026-06-01","2026-06-02"])
timeser=pd.to_datetime(ser)
print(timeser)

# Create two DataFrames, df1 and df2

df1=pd.DataFrame({
    "ID":[101,102,103,104,105],
    "Department":["HR","Finance","HR","Marketing","Sales"]
})
df2=pd.DataFrame({
    "ID":[103,104,105,106,107],
    "City":["Mumbai","Jaipur","Ajmer","Jaipur","Delhi"]
})
print("Df1:",df1)
print("Df2:",df2)

inner=pd.merge(df1,df2,on='ID',how='inner')
print(inner)

left=pd.merge(df1,df2,on='ID',how='left')
print(left)

right=pd.merge(df1,df2,on='ID',how='right')
print(right)

df1_index = df1.set_index('ID')
df2_index = df2.set_index('ID')
joined = df1_index.join(df2_index)
print(joined)

df3 = pd.DataFrame({
    'ID': [101,104,105,108,109],
    'Department': ["HR","Finance","HR","Marketing","Sales"],
    'Bonus': [5000, 6000, 5500, 7000,8000]
})

multi_key=pd.merge(df1,df3,on=['ID','Department'],how='inner')
print(multi_key)

# create three dataframes

df4 = pd.DataFrame({
    'ID':[106,107],
    'Department':['IT','Admin']
})
combined=pd.concat([df1,df4],axis=0)
print(combined)

final=pd.merge(combined,df3,on='ID')
print(final)