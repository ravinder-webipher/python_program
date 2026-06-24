# dice guess program
print('------------------------dice program----------------------')
#throw dice that generates 2 random numbers
n1,n2=5,4
n3=n1+n2

for i in range(1,4):
    guess=int(input("Enter guess: "))
    if guess==n3:
        print("wow you won in ",i," attempt")
        break
    else:
        print("Try again")
if guess!=n3:
    print("You have exhaused all the attempts. Try your luck next time")
        

