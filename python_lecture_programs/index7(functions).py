#functions with arguments/paramters and with return value
def get_student_result(sub1, sub2):
    tot_marks=sub1+sub2
    if tot_marks>=100:
        return "pass"
    else:
        return "fail"
    
result=get_student_result(50,90)
print("result of student is ",result)

#functions with no arguments/paramters and with no return value
def get_student_result():
    sub1=50
    sub2=90
    tot_marks=50+90
    if tot_marks>=100:
         print("pass")
    else:
        print("fail")
    
get_student_result()

#functions with arguments/paramters but with no return value
def get_student_result(sub1,sub2): # local variables
    tot_marks=sub1+sub2
    if tot_marks>=100:
         print("pass")
    else:
        print("fail")
    
get_student_result(50,40)

#functions with no arguments/paramters but with return value
sub1=50 #global variables
sub2=40 #global variables
def get_student_result():
    tot_marks=sub1+sub2
    if tot_marks>=100:
        return "pass"
    else:
        return "fail"
    
result=get_student_result()
print("Result of student is ", result)
#ternary operator
print("promoted to next class"  if result=="pass" else "not promoted to next class")




























