# for loop
print("----------range-------------------")
for i in range(10):
    print (i)
    
print("----------range2-------------------")    
for i in range(1,10):
    print(i)

print("----------range3-------------------")  
for i in range(1,10,2):
    print(i) 
    
print("----------range4-------------------")  
for i in range(-3,4):
    print(i) 
    
print("----------range5-------------------")  
for i in range(-3,-1):
    print(i) 

print("----------range6-------------------")  
for i in range(-3,-5):
    print(i) 
    
print("----------range7------------------")  
for i in range(-3,-5,-1):
    print(i) 
    
print("----------string-------------------")  
for i in "ravinder":
    print(i) 
    
#id function
print('--------------------id function------------')
a,b,c=5,10,20
print (id(a))
print (id(b))
print (id(c))

#identity operator
print('-------------integer identity operator------------')
a,b,c=10,20,10.0
print(a is b)
print(a is c)
print(a==b)
print(a==c)
print(a is not b)
print('-------------------------string identity operator')
a,b,c='ravi','ram','ravi'
print(a==b)
print(a==c)
print(a is b)
print(a is c)

print('------------break and continue in loop')

for i in range(1,10):
    if i==5:
        #break
        continue
    print(i)
