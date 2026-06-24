#program to calculate bill with discount
print("------------calculate bill with discount applied--------------")
price=int(input("Enter price "))
qty=int(input("Enter qunatity "))
dscnt=0
grBill=price*qty
if grBill>5000 and qty>3:
    dscnt=grBill*10/100
netBill=grBill-dscnt
print("Gross Bill ", grBill)
print("Discount   ", dscnt)
print("Net Bill   ", netBill)