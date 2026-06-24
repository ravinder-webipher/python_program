#program to calculate telephone bill
print("------------calculate telephone bill--------------")
ct_no=int(input("Enter contact no "))
no_of_calls=int(input("Enter no of calls "))

if no_of_calls>=1 and no_of_calls<=100:
    price=1*no_of_calls
elif no_of_calls>=101 and no_of_calls<=200:
    price=(1*100)+(0.5*(no_of_calls-100))
elif no_of_calls>=201 and no_of_calls<=300:
    price=(1*100)+(0.5*100)+(0.25*(no_of_calls-200))
elif no_of_calls>300:
    price=(1*100)+(0.5*100)+(0.25*100)+(0.10*(no_of_calls-300))
print("Gross Bill ", price)
tax=price*18/100
print("tax ", tax)
ntBill=price+tax
print("net Bill ", ntBill)