# Accept any city name from the user and display monument of that city 
print("------------------- display monument based on city name----------------------")
cty=input("Enter city name ")
if cty=='delhi':
    print("monument in ",cty, "is ","red fort")
elif cty=='Jaipur':
    print("monument in ",cty, "is ","Jai Mahal")
elif cty=='amritsar':
    print("monument in ",cty, "is ","Golden Temple")
elif cty=='agra':
    print("monument in ",cty, "is ","taj mahal")
else:
    print("city name is incorrect or it does not have any monument")
