#personal details
print('----------------------------personal details------------------')
name=input("Enter your name ")
gender=input("Enter your gender ")
age=int(input("Enter your age "))
address=input("Enter your address ")
city=input("Enter your city ")
state=input("Enter your state ")
pincode=input("Enter your pin code ")
print()

#age and password validation
if age>=18:
    print("Age validation completed. Go to next step")
    print()
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
        print()
        print('----------Terms and conditions----------------')
        print("1. Participants must provide correct and complete registration details. Please tick Y or N ")
        print("2. Each participant is allowed to register and play only once. ")
        print("3. The quiz must be completed within the specified time limit.  ")
        print("4. Any attempt to manipulate or hack the system will lead to immediate disqualification.  ")
        print("5. The organizer reserves the right to disqualify any participant found violating the rules..  ")
        print("6. The organizer's decision regarding scores and winners will be final and binding.  ")
        print("7. The organizer reserves the right to modify, suspend, or cancel the quiz at any time.  ")
        print()
        tick=input("Please click Yes if you accept all the conditions. else press No: ")
        print()
        
        if tick=='Yes':
            print("Entering game: ")  
            tickYes=True
        else:
            print("You can't play game.")
            print()

    # #quiz questions
    if tickYes is True:
        cr_ans=0
        print("1. What is Python")
        print("a) A web browser") 
        print("b) A programming language")
        print("c) An operating system")
        print("d) A database")
        print()
        for i in range(1,3):
            answer=input("Answer: ")
            if answer=='b':
                print("Correct answer: b")
                cr_ans+=1
                break
            else:
                print("Incorrect.") 

        print()
        print("2. Who developed Python programming language")
        print("a) Dennis Ritchie")
        print("b) James Goslingn")
        print("c) Guido van Rossum")
        print("d) Bjarne Stroustrup") 
        print()
        for i in range(1,3):
            answer=input("Answer: ")
            if answer=='c':
                print("Correct answer: c")
                cr_ans+=1
                break
            else:
                print("Incorrect. Try again")
                
        print()
        print("3 What is the extension of python file")
        print("a) .python")
        print("b) .py") 
        print("c) .pt") 
        print("d) .pyt")
        print()
        for i in range(1,3):
            answer=input("Answer: ")
            if answer=='b':
                print("Correct answer: b")
                cr_ans+=1
                break
            else:
                print("Incorrect. Try again")
                
        print()
        print("4. Which function is used to take input from user in python")
        print("a) read()")
        print("b) scan()")
        print("c) input()") 
        print("d) print()")
        print()
        for i in range(1,3):
            answer=input("Answer: ")
            if answer=='c':
                print("Correct answer: c")
                cr_ans+=1
                break
            else:
                print("Incorrect. Try again")
                
        print()
        print("5. Which function is used to display output in python")
        print("a) read()")
        print("b) scan()") 
        print("c) input()") 
        print("d) print()")
        print()
        for i in range(1,3):
            answer=input("Answer: ")
            if answer=='d':
                print("Correct answer: d")
                cr_ans+=1
                break
            else:
                print("Incorrect. Try again")
                
        print()
        print("6. Which symbol is used to write a single-line comment in Python")
        print("a) //")
        print("b) #")
        print("c) /* */")
        print("d) --")
        print()
        for i in range(1,3):
            answer=input("Answer: ")
            if answer=='b':
                print("Correct answer: b")
                cr_ans+=1
                break
            else:
                print("Incorrect. Try again")
                
        print()
        print("7. Which loop is mostly used in python")
        print("a) for loop")
        print("b) while loop")
        print("c) All of the above")
        print("d) None of the above")
        print()
        for i in range(1,3):
            answer=input("Answer: ")
            if answer=='a':
                print("Correct answer: a")
                cr_ans+=1
                break
            else:
                print("Incorrect. Try again")
    
        cr_ans_per=cr_ans/7*100
        print()
        print("Quiz completed. your score is ",int(cr_ans_per)," percent.")
        print()
    
    
else:
    print("You are under age. You can't play game.")
    print()