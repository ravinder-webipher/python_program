#tuples
a=(10,20,'chips',50,90,'burger',80.55,65.0)

print(a,type(a))
print(a[2])
print(a[4])
print("slicing: ",a[0:4])
print("slicing2: ",a[0:5:2])
print("slicing3: ",a[-3:-8:-1])
#single value
a=(10)

print("single value: ",a,type(a))
a=(10,)#single value
print("single value after applying comma: ",a,type(a))
a=()
print("blank value: ",a)

#multiple values printing
a=(10,20,'chips',50,90,'burger',80.55,65.0)
print(a[0],a[2])
v1,v2,v3,v4,v5,v6,v7,v8=a
print("variable values are:",v1)
print("variable values are:",v2)
print("variable values are:",v3)
print("variable values are:",v4)
print("variable values are:",v5)
print("variable values are:",v6)
print("variable values are:",v7)
print("variable values are:",v8)

#print multiple values using for loop
print()
for i in range(8):
    print("values after applying for loop are: ",a[i])
    
print()
#print multiple values using for loop
for i in a:
    print("values after applying next for loop: ",i)
#print values using while loop
print()
j=0
while j<8:
    print("values after applying while loop are: ",a[j])
    j+=1
    
#mutable or immutable
print("before change: ",a[5])
# this will give error
#a[5]="ravi"
#print ("after change: ",a[5])








