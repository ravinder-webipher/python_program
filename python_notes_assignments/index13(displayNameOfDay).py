#  to accept a number from 1 to 7 and display the name of the day like 1 for "sunday " , 2 for "Monday" etc.
print("------------------- Enter number from 1 to 7 and display the name of the day----------------------")
a=int(input("Enter number "))
if a==1:
    print("Sunday")
elif a==2:
    print("Monday")
elif a==3:
    print("Tuesday")
elif a==14:
    print("Wednesday")
elif a==5:
    print("Thursday")
elif a==6:
    print("Friday")
elif a==7:
    print("Saturday")
else:
    print("Enter day between 1 and 7 only")

