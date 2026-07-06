#inventory module

print("----------------------------Inventory module--------------------------")
print()

#functions body
def add_stocks():
    print("Add stocks")
    print()
    click='yes'
    while click.lower()=='yes':
        item=input("Enter item name: ")
        qt=int(input("Enter quantity: "))
        price=int(input("enter price: "))
        print("do you want to add another item.") 
        click=input("please type yes or no: ")
        if click.lower()=='no':
            break
        while click.lower()!='yes' and click.lower()!='no':
            click=input("please type yes or no: ")
    
def view_stocks():
    #define dictonaries for stocks
    item=[
        { 
         "name":"bhujia",
         "qt":10,
         "price":75},
        {
         "name":"biscuit",
         "qt":5,
         "price":25
        },
        {
         "name":"chips",
         "qt":10,
         "price":75
        },
        {
         "name":"icecream",
         "qt":8,
         "price":20
        }
    ]
    
    print("view stocks")
    print()
    #item_name=input("Enter item name: ")
    print()
    for item1 in item:
        item_name=input("Enter item name: ")
        if item_name in item1.values():
            print("Found in stock. details are:")
            for item_key,item_value in item1.items():
                print(item_key,":",item_value)
            break
    else:
        print("item not found in stocks. Please enter correct entry")
    


#password validation
print()
pwd_correct=False
tickYes=False
for i in range(1,4):
    login_id=input("enter login id: ")
    pwd=input("Enter password ")
    if login_id=='ravinder' and pwd=='ravi':
        print("Password is correct. go to next step ")
        pwd_correct=True
        break
    else:
        print("Invalid login id or password. Please try again")
        print()

if pwd_correct is True:
    choice=input("please type add or view for add and view stocks respectively: ")
    if choice.lower()=='add':
        add_stocks()
    elif choice.lower()=='view':
        view_stocks()
    else:
        print("wrong entry. exiting from the application")
        


