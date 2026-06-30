#program to manage inventory
def stock_dtls_biscuit(bs_type):
    product=['britannia marie gold','parle-g','monaco','oreo','good day']
    if bs_type in product:
        print("In stock")
    else:
        print("out of stock")
    
bs_type=input("Enter biscuit type ")
    
stock_dtls_biscuit(bs_type)