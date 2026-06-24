#  Program to accept a table no and print it using the loop concept
print("----------------Accept table number and print table-----------")

table_no=int(input("Enter table no "))
for i in range(1,11):
    result=table_no*i
    print(table_no," * ",i," = ",result)