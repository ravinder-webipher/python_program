#quiz program

print('----------------------------quiz program------------------')
name=input("Enter your name ")
gender=input("Enter your gender ")
age=int(input("Enter your age "))
address=input("Enter your address ")
city=input("Enter your city ")
state=input("Enter your state ")
pincode=input("Enter your pin code ")

#age and password validation
if age>=18:
    print("\nAge validation completed. Go to next step")
    pwd_correct=False
    tickYes=False
    for i in range(1,4):
        pwd=input("Enter password ")
        cpwd=input("Enter confirm password ")
        if pwd==cpwd:
            print("Password is correct. go to next step ")
            pwd_correct=True
            break
        else:
            print("Invalid password. Please try again")
            
    #Terms and conditions
    if pwd_correct is True:
        print('\n----------Terms and conditions----------------')
        print("1. Participants must provide correct and complete registration details. Please tick Y or N ")
        print("2. Each participant is allowed to register and play only once. ")
        print("3. The quiz must be completed within the specified time limit.  ")
        print("4. Any attempt to manipulate or hack the system will lead to immediate disqualification.  ")
        print("5. The organizer reserves the right to disqualify any participant found violating the rules..  ")
        print("6. The organizer's decision regarding scores and winners will be final and binding.  ")
        print("7. The organizer reserves the right to modify, suspend, or cancel the quiz at any time.  ")
        tick=input("\nPlease click Yes if you accept all the conditions. else press No: ")
        if tick=='Yes':
            print("\nEntering game: \n")
            tickYes=True
        else:
            print("You can't play game.")

    # #quiz questions
    if tickYes is True:
        cr_ans=0
        print("1. What is Python")
        print(" a) A web browser\n b) A programming language\n c) An operating system\n d) A database")  
        for i in range(1,3):
            answer=input("\nAnswer: ")
            if answer=='b':
                print("Correct answer: b")
                cr_ans+=1
                break
            else:
                print("Incorrect.") 
        print("\n2. Who developed Python programming language")
        print(" a) Dennis Ritchie\n b) James Goslingn\n c) Guido van Rossum\n d) Bjarne Stroustrup") 
        for i in range(1,3):
            answer=input("\nAnswer: ")
            if answer=='c':
                print("Correct answer: c")
                cr_ans+=1
                break
            else:
                print("Incorrect. Try again")
        print("\n3 What is the extension of python file")
        print(" a) .python\n b) .pt\n c) .py\n d) .pyt")  
        for i in range(1,3):
            answer=input("\nAnswer: ")
            if answer=='c':
                print("Correct answer: c")
                cr_ans+=1
                break
            else:
                print("Incorrect. Try again")
        print("\n4. Which function is used to take input from user in python")
        print(" a) read()\n b) scan()\n c) input()\n d) print()")
        for i in range(1,3):
            answer=input("\nAnswer: ")
            if answer=='c':
                print("Correct answer: c")
                cr_ans+=1
                break
            else:
                print("Incorrect. Try again")
        print("\n5. Which function is used to display output in python")
        print(" a) read()\n b) scan()\n c) input()\n d) print()")
        for i in range(1,3):
            answer=input("\nAnswer: ")
            if answer=='d':
                print("Correct answer: d")
                cr_ans+=1
                break
            else:
                print("Incorrect. Try again")
        print("\n6. Which symbol is used to write a single-line comment in Python")
        print(" a) //\n b) #\n c) /* */\n d) --")  
        for i in range(1,3):
            answer=input("\nAnswer: ")
            if answer=='b':
                print("Correct answer: b")
                cr_ans+=1
                break
            else:
                print("Incorrect. Try again")
        print("\n7. Which loop is mostly used in python")
        print(" a) for loop\n b) while loop\n c) All of the above\n d) None of the above")
        for i in range(1,3):
            answer=input("\nAnswer: ")
            if answer=='a':
                print("Correct answer: a")
                cr_ans+=1
                break
            else:
                print("Incorrect. Try again")
        cr_ans_per=cr_ans/7*100
        print("\nQuiz completed. your score is ",int(cr_ans_per)," percent.")
    
    
else:
    print("\nYou are under age. You can't play game.")