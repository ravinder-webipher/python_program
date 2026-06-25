# To calculate greatest of three numbers
print("-------------------calculate greatest of three numbers-----------------------")
a=int(input("Enter First number "))
b=int(input("Enter Second number "))
c=int(input("Enter Third number "))

if a>b and a>c:
    print("greatest number is ", a)
elif b>a and b>c:
    print("greatest number is ",b)
elif c>a and c>b:
    print("greatest number is ",c)
elif a>b and a==c:
    print("both first and third numbers are greatest")
elif a>c and a==b:
    print("both first and second numbers are greatest")
elif b>a and b==c:
    print("both second and third numbers are greatest")  
else:
    print("all numbers are equal")
    