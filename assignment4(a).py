#a CSV file for address book, CSV file should have column for name, address, mobile, email.

import csv

book=[['Name','Address','Mobile','Email']]

with open("data.csv","w",newline='') as file:
    writer=csv.writer(file)

    writer.writerow(book[0])

    for i in range(3):
        print("Enter details")
        name=input("Enter name:")
        address=input("Enter address:")
        mobile=int(input("Enter mobile number:"))
        email=input("Enter email:")

        book.append([name, address, mobile, email])

        writer.writerow([name,address,mobile,email])

for row in book:
        print(row)


    


   