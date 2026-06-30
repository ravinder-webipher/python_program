print('--------------print list--------------')
# a="ram","ravi","sham"
# print(a)
# print(type(a))

product=['burger','pizza','momos','noodles']
print(type(product))
print(product)
choice=input("Enter choice ")
if choice in product:
    print('In stock')
else:
    print('Out of stock')
    
