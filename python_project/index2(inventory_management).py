#inventory module

print("----------------------------Inventory module--------------------------")
print()

stock_list = [
]       
#add stocks function
def add_stocks(stock_list):
    print("Add stocks")
    print()
    click='yes'
    while click.lower()=='yes':
        item=input("Enter item name: ")
        qt=int(input("Enter quantity: "))
        price=int(input("enter price: "))
        stock_list.append({
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
    
    print("Stock items successfully added")

#delete stocks function
def del_stocks(stock_list):
    print("Delete stocks")
    print()
    click='yes'
    while click.lower()=='yes':
        item_name=input("Enter item name: ")
        for item in stock_list:
            if item_name==item["item_name"]:
                stock_list.remove(item)
                print("Stock items successfully deleted")
                break
        else:
            print()
            print("item not found")
        print("do you want to delete another item.") 
        click=input("please type yes or no: ")
        if click.lower()=='no':
            break
        while click.lower()!='yes' and click.lower()!='no':
            click=input("please type yes or no: ")
    
#view stocks function  
def view_stocks(stock_list):
    print("view stocks")
    print()
    click='yes'
    while click.lower()=='yes':
        item_name=input("Enter item name: ")
        for item1 in stock_list:
            if item_name==item1["item_name"]:
                print()
                print("Found in stock. details are:")
                for item_key,item_value in item1.items():
                    print(item_key,":",item_value)
                break
        else:
            print("Item not found in stocks")
        print("do you want to view another item.") 
        click=input("please type yes or no: ")
        while click.lower()!='yes' and click.lower()!='no':
            click=input("please type yes or no: ")
        if click.lower()=='no':
            break
        
#buy items function
def buy_items(stock_list):
    print()
    click='yes'
    cart = []
    while click.lower()=='yes':
        item_name=input("Please select item you want to purchase: ")
        for item in stock_list:
            if item_name==item["item_name"]:
                print()
                cart.append(item)
                print("item found in stock. Added to your cart")
                break
        else:
            print()
            print("item not found in stocks.")
        print("do you want to purchase another item.") 
        click=input("please type yes or no: ")
        while click.lower()!='yes' and click.lower()!='no':
            click=input("please type yes or no: ")
        if click.lower()=='no':
            print("ok. proceeding you to the payment page")
            break
    return cart

#calculate bill function           
def calculate_bill(cart):
    print("\n------------Calculate Bill--------------")

    total_gross = 0

    print("Items Purchased")
    print("---------------------------")

    for item in cart:
        name = item["item_name"]
        qty = item["item_qty"]
        price = item["item_price"]
        amount = price * qty
        total_gross += amount
        print("Item Name :", name)
        print("Price     :", price)
        print("Quantity  :", qty)
        print("Amount    :", amount)
        print("---------------------------")

    # Apply discount on total bill
    if total_gross > 200:
        total_discount = total_gross * 10 / 100
    else:
        total_discount = 0

    net_bill = total_gross - total_discount

    print("Gross Bill:", total_gross)
    print("Discount:", total_discount)
    print("Net Bill:", net_bill)
    
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

    while True:
        pwd_correct = password_validation()
        if not pwd_correct:
            print("Password incorrect.")
            break
        role = input("Please enter role (admin/user): ").lower()
        if role == "admin":
            choice = input("Add stocks (yes/no): ")
            if choice == "yes":
                add_stocks(stock_list)
            choice = input("Delete stocks (yes/no): ")
            if choice == "yes":
                del_stocks(stock_list)
            choice = input("View stocks (yes/no): ")
            if choice == "yes":
                view_stocks(stock_list)
        elif role == "user":
            choice = input("View stocks (yes/no): ")
            if choice == "yes":
                view_stocks(stock_list)
            choice = input("Buy items (yes/no): ")
            if choice == "yes":
                cart = buy_items(stock_list)
                calculate_bill(cart)
        else:
            print("Invalid role.")
        again = input("\nDo you want to login again? (yes/no): ").lower()
        while again not in ("yes", "no"):
            again = input("Please type yes or no: ").lower()
        if again == "no":
            print("Thank you. Exiting the application.")
            break
                
main()
        