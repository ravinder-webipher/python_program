#To accept a CVV number of a card of the customer and print transaction based upon it
print("----------print transaction based on CVV number entered-------------")
n1=input("Enter card number ")
cvv_no=int(input("Enter CVV number of card "))
if cvv_no>0:
    print("CVV number is correct. going to print transactions details")
else:
    print("CVV number is incorrect.")