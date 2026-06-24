#program to calculate student marks and grade
print("------------calculate student marks and grade--------------")
st_name=input("Name ")
cls=input("Class ")
sct=input("Section ")
eng=int(input("English "))
hindi=int(input("Hindi "))
pun=int(input("Punjabi "))
mths=int(input("Maths "))
cmp=int(input("Computer "))
totMarks=eng+hindi+pun+mths+cmp
avg=totMarks/5

print("Name ", st_name)
print("Class ", cls)
print("Section ", sct)
print("Total Marks ",totMarks)
print("Average ",avg)

if avg>=90:
    print("Grade Outstanding")
elif avg>=80 and avg<=90:
    print("Grade Very Good")
elif avg>=60 and avg<=80:
    print("Grade Good")
elif avg>=50 and avg<=60:
    print("Grade Fair")
elif avg<50:
    print("Grade Participation")

