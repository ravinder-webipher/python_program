# quiz program

print('----------------------------quiz program------------------')

#name=input("Enter your name ")
age=int(input("Enter your age "))
# dob=int(input("Enter your date of birth "))
# address=input("Enter your address ")
# city=input("Enter your city ")
# state=input("Enter your state ")
# pincode=input("Enter your pin code ")

if age>=18:
    print("\nAge validation completed. Go to next step")
    pwd_correct=False
    for chnces in range(1,4):
        pwd=input("Enter password ")
        cpwd=input("Enter confirm password ")
        if pwd==cpwd:
            print("Password is correct. go to next step ")
            pwd_correct=True
            break
        else:
            print("invalid password. Please try again.")
            
    if pwd_correct==True:
        print('\n----------Terms and conditions----------------')   
else:
    print("\nYou are under age. You can't play game.")