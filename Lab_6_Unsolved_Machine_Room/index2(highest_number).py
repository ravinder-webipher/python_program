#  Program to accepts 10 number from user and display the highest number
print("----------------Accept 10 number and display highest number-----------")
highest=0
for i in range(1,11):
    no=int(input("Enter number "))
    if no>highest:
        highest=no
        print(highest)
    print("highest number is ",highest)
