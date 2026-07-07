#inventory module

print("----------------------------Inventory module--------------------------")
print()

#functions body

def add_stocks():
    dict_objects_add=[]
    print("Add stocks")
    print()
    click='yes'
    while click.lower()=='yes':
        item=input("Enter item name: ")
        qt=int(input("Enter quantity: "))
        price=int(input("enter price: "))
        dict_objects_add.append({
            "item_name":item,
            "item_qty":qt,
            "item_price":price
        })
        print("do you want to add another item.") 
        click=input("please type yes or no: ")
        if click.lower()=='no':
            break
        while click.lower()!='yes' and click.lower()!='no':
            click=input("please type yes or no: ")
    
    print("Stock item successfully added")
    return dict_objects_add


    
    
def view_stocks(dict_objects_vw):
    print("view stocks")
    print()
    dict_objects_vw=[dict_objects_vw]
    item_name=input("Enter item name: ")
    for item1 in dict_objects_vw:
        if item_name in item1.values():
            print("Found in stock. details are:")
            print()
            for item_key,item_value in item1.items():
                print(item_key,":",item_value)
            break
    else:
        print("item not found in stocks. Please enter correct entry")
    
#password validation   
def password_validation():
    print()
    pwd_correct=False
    tickYes=False
    for i in range(1,4):
        login_id=input("enter login id: ")
        pwd=input("Enter password ")
        if login_id=='ravinder' and pwd=='ravi':
            print("Password is correct. go to next step ")
            pwd_correct=True
            return pwd_correct
        else:
            print("Invalid login id or password. Please try again")
            print()
def main():
    dict_objects={}
    pwd_correct=False
    pwd_correct=password_validation()
    if pwd_correct is True:
            choice=input("Do you want to add stocks. please type yes or no: ")
            if choice.lower()=='yes':
                dict_objects=add_stocks()
                print(dict_objects,type(dict_objects))
                choice=input("Do you want to view added stocks. please type yes or no: ")   
                if choice.lower()=='yes':
                    view_stocks(dict_objects)
            else:
                print("ok. exiting from the application")
                
main()
        