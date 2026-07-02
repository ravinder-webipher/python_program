'''
products_price={
    "chips1":10,
    "buiscuit":"30",
    "bhujia":50,
    "cold drink":100  
}
print(products_price, type(products_price))
print("price of chips is: ", products_price["chips1"])
print("price of cold drink is: ", products_price["cold drink"])
print()
#for loop
for i in products_price:
    print("price of " ,i, "is: ",products_price[i])
    
student_dtls={
    "student name": "ravi",
    "age":20,
    "class":"6th",
    50:"roll no",
    "age":50,
    "height":30,
    "marks":30
}

print("student class is: ",student_dtls["class"])
print("student roll no is: ",student_dtls[50])
print("student age is: ",student_dtls['age'])
print("student height is: ",student_dtls['height'])
print("student marks are: ",student_dtls['marks'])
'''
employee_details={
    "name":"ravinder",
    "id":102,
    "salary":10000,
    "department":"IT"
}

emp_dtls=input("Please type which employee details you required: ")

if emp_dtls in employee_details:
    print("found")
    print("employee ",emp_dtls," is ",employee_details[emp_dtls])
else:
    print("wrong details")