import sqlite3
conn = sqlite3.connect("supermarket.db")

data='''
CREATE TABLE PRODUCTS(
p_id integer primary key,
p_name varchar(50),
price integer,
category varchar(20)
)
'''

data1='''
CREATE TABLE ORDERS(
ord_id integer primary key,
cust_name varchar(50),
p_name varchar(20)
)
'''

data2='''
CREATE TABLE CUSTOMER(
cust_id integer primary key,
cust_name varchar(50),
mobile integer,
city varchar(20)
)'''

conn.execute(data)
conn.execute(data1)
conn.execute(data2)

conn.execute("""Insert into products(p_id,p_name,price,category) values
(101,'Laptop',150000,'Electronics'),
(102,'Mobile',25000,'Electronics'),
(103,'Watch',10000,'Accessories')""")

conn.execute("""Insert into orders(ord_id,cust_name,p_name) values
(1,'Rajesh','Laptop'),
(2,'Priya','Mobile'),
(3,'Aman','Watch')""")

conn.execute("""Insert into customer(cust_id,cust_name,mobile,city) values
(1001,'Rajesh',9876543210,'Jaipur'),
(1002,'Priya',9988776655,'Delhi'),
(1003,'Aman',9871234567,'Mumbai')""")

conn.commit()

print("PRODUCTS TABLE")
cur = conn.execute("SELECT * FROM PRODUCTS")
for row in cur:
    print(row)

print("\nPRODUCTS PRICE GREATER THAN 20000")
cur = conn.execute("SELECT * FROM PRODUCTS WHERE price > 20000")
for row in cur:
    print(row)

print("\nCUSTOMER TABLE")
cur = conn.execute("SELECT * FROM CUSTOMER")
for row in cur:
    print(row)

print("\nORDERS TABLE")
cur = conn.execute("SELECT * FROM ORDERS")
for row in cur:
    print(row)

conn.execute("UPDATE PRODUCTS SET price = 30000 WHERE p_name='Mobile'")
conn.commit()
print("\nAFTER UPDATE")
cursor = conn.execute("SELECT * FROM PRODUCTS")
for row in cursor:
    print(row)


conn.execute("DELETE FROM CUSTOMER WHERE cust_name='Aman'")
conn.commit()
print("\nAFTER DELETE")
cursor = conn.execute("SELECT * FROM CUSTOMER")
for row in cursor:
    print(row)

conn.close()




