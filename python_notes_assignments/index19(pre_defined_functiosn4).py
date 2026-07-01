# ljust()
# rjust()
# zfill()
# replace()
# join()
fruits=["banana","mango","cherry"]
def fruit_name():
    fr=input("enter fruit name: ")
    qt=input("enter mango quantity: ")
    print("left justified is: ",fr.ljust(10,"*"))
    print("right justified is: ",fr.rjust(10,"*"))
    print("zfill is: ",qt.zfill(2))
    print("replace with another fruit: ",fr.replace(fr,"banana"))
    print("join fruit with pipe: ","|".join(fruits))
    
fruit_name()
