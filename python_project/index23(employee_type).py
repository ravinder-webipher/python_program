emp_list=[
    {"name":"ravinder","id":201,"type":"permanent","salary":60000},
    {"name":"ram","id":202,"type":"intern","salary":15000},
    {"name":"sham","id":203,"type":"intern","salary":20000},
    {"name":"sita","id":204,"type":"permanent","salary":50000},
    {"name":"geeta","id":205,"type":"intern","salary":15000}
]
class employee:
    def __init__(self,empName,eid):
        self.empName=empName
        self.eid=eid
    def emp_dtls(self):
        print()
        for i in emp_list:
            if self.eid==i["id"]:
                print()
                print("Employee details are:")
                for emp_key,emp_values in i.items():
                    print(emp_key,":",emp_values)
                break    
    def approve_leave(self):
        for i in emp_list:
            if self.eid in i.values():
                print("leave approved")
                break
    def get_emp_type(self):
        for i in emp_list:
            if self.eid in i.values():
                return i["type"]
                  
class permEmp():
    def __init__(self,empName,eid):
        self.empName=empName
        self.eid=eid
    def perm_salary_increment(self):
        incr_sal=int(input("How much salary do you want to increase: "))
        print()
        for i in emp_list:
            if self.eid==i["id"]:
                print(self.empName,"current salary is:",i["salary"])
                i["salary"]=i["salary"]+incr_sal
                print(self.empName,"revised salary is:",i["salary"])
            break


class internEmp():
    def __init__(self,empName,eid):
        self.empName=empName
        self.eid=eid
    def intern_salary_increment(self):
        for i in emp_list:
            if self.eid==i["id"]:
                if i["type"]=="intern":
                    print(self.empName,"is intern. Hence his salary cannot be incremented.")


#***************driver code*****************      
i=0
while i<3:
    i+=1
    ename = input("Enter employee name: ")
    empId = int(input("Enter employee id: "))
    obj_emp = employee(ename, empId)
    empType = obj_emp.get_emp_type()
    if empType is None:
        print("Employee does not exist. Please enter again.")
        print()
    else:
        break
if empType is None:
    print("Maximum attempts reached.")
else:
    obj_emp=employee(ename,empId)
    obj_emp.emp_dtls()
    print()
    emp_leave_apply=input("Apply leave. (yes/no) ")
    if emp_leave_apply.lower()=='yes':
        obj_emp.approve_leave()
    else:
        print("ok. go to next step")
    print()
    # permanent employee
    if empType.lower()=='permanent':
        click=input(f"Do you want to increase {ename} salary (yes/no) ")
        if click=="yes":
            obj_perm_emp=permEmp(ename,empId)
            obj_perm_emp.perm_salary_increment()
        else:
            print("ok. exiting from the application")
    elif empType.lower()=='intern':
        click=input(f"Do you want to increase {ename} salary (yes/no) ")
        if click=="yes":
            obj_intern_emp=internEmp(ename,empId)
            obj_intern_emp.intern_salary_increment()
        else:
            print("ok. exiting from the application")