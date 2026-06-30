'''
a=10
b=20
if a>b:
    print("a is greatest")
else:
    print("b is greatest")
print("program ends")
'''
# card program
'''
print("------------------------------user details program----------------------------------")
age=int(input("Enter Age: "))
if age>18:
    print("user valid")
    pswd=input("enter password: ")
    cpswd=input("enter confirm password: ")
    if pswd==cpswd:
        print("password match")
    else:
        print("password not matched")
else:
    print("age not matched.")
    cvv=int(input("enter CVV: "))
    if cvv>0:
        print("card details matched. doing next process. Please wait.")
    else:
        print("card details not matched")
print("\nProgram ends\n")
'''
'''
# elif program
print("--------------------------------------decision making program-----------------------------------")
day=int(input("enter day: "))
if day==1:
    print("DBA meeting with oracle at 10 am CST")
elif day==2:
    print("DBA Internal team meeting")
elif day==3:
    print("Meeting with Dev Team")
elif day==4:
    print("Meeting with stake holders")
elif day==5:
    print("Whole IT team meeting")
else:
    print("Enter day between 1 to 5 only")
'''
'''
#loop program
i=1
while i<10:
    print("while loop executes")
    i+=1
 '''   
#break continue 

while True:
    n1=int(input("Enter no 1: "))
    n2=int(input("Enter no 2: "))
    print("sum of two numbers is: ",n1+n2)
    choice=input("Do you want to continue adding: press y or n: ")
    if choice=='y':
        continue
    elif choice=='n':
        break
    else:
        print("enter choice between y and n only")