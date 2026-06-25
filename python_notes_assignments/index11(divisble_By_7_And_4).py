# o check whether the number is divisible by both 7 and 4 or not
print("-------------------calculate number is divisible by both 7 and 4----------------------")
a=int(input("Enter number "))
if a%7==0 and a%4==0:
    print("Entered number is divisble by 7 and 4 ")
elif a%7==0 or a%4==0:
    print("Entered number is divisible by 7 or 4 ")
else:
    print("Entered number is not divisble by 7 and 4")
