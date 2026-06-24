#program to find greatest number
print("------------calculate bill with discount applied--------------")
n1=int(input("Enter first number "))
n2=int(input("Enter second number "))
n3=int(input("Enter third number "))
if n1>n2 and n1>n3:
    print("no ",n1, " is greatest")
elif n2>n1 and n2>n3:
    print("no ",n2, " is greatest")
elif n3>n1 and n3>n2:
    print("no ",n3, " is greatest")
elif n1==n2 and n1>n3:
    print("no ",n1, " is greatest")
elif n1==n3 and n1>n2:
    print("no ",n1, " is greatest")
elif n2>n1 and n2==n3:
    print("no ",n2, " is greatest")
else:
    print("All numbers are equal")