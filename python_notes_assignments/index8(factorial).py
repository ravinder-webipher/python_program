# Progeam to calculate factorial of 5
print("-------------------calculate factorial of 5 -----------------------")
a=int(input("enter number "))
b=1
fact=a
while a>0:
    b*=a
    a-=1
print ("factorial of ",fact, " is ", b)