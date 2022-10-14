# My GitHub:  		GitHub.com/AliRezaJoodi
# Source Link:  	W3Schools.com/python/ref_string_join.asp

myTuple = ("John", "Peter", "Vicky")
myStr = "-".join(myTuple)
print("myStr Value: ",myStr)
print("myStr Type:  ",type(myStr))

myList = ['(', '*', '+', 'C', 'w', 'J', '5', '$']
myStr = "".join(myList)
print("myStr Value: ",myStr)

# When using a dictionary as an iterable, the returned values are the keys, not the values.
myDict = {"name": "John", "country": "Norway"}
mySeparator = "+"
myStr = mySeparator.join(myDict)
print(myStr)