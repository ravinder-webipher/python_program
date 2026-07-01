#islower
#istitle
#isalpha
#isalnum
#isdigit
#isspace
def product_dtls():
    pr1=input("Enter product: ")
    print("product entered is in lower case : ",pr1.islower())
    print("product entered is in upper case : ",pr1.isupper())
    print("product entered following title : ",pr1.istitle())
    print("product entered are all alphabets : ",pr1.isalpha())
    print("product entered are alpha numeric : ",pr1.isalnum())
    print("product entered are digits : ",pr1.isdigit())
    print("product entered are all white spaces : ",pr1.isspace())
    
product_dtls()
