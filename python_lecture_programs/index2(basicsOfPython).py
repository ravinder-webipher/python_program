#variables

a=10
b=20

print(type(a))
print (type(b))
print(a+b)

a='ram'
b='sham'

print(type(a))
print (type(b))

a=1.2
b=2.5

print(type(a))
print (type(b))
print (a+b)

#bill calculation
#by default input function takes input as string. so we need to convert it into int using int function
product=input('enter product name: ')
price=int(input('enter pricechips: '))
qty=int(input('enter quantity: '))
print("price is ",qty*price)