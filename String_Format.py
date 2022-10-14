# My GitHub:  		GitHub.com/AliRezaJoodi
# Source Link:  	W3Schools.com/python/python_strings_format.asp

age = 36
txt = "Bab is " + str(age) + " years old."
print(txt)  

txt = "Bab is {} years old."
print(txt.format(age)) 

print(f"Bab is {age} years old.") 

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price)) 

myorder = "I want {1} pieces of item {2} for {0} dollars."
print(myorder.format(price, quantity, itemno)) 
