# My GitHub:  		GitHub.com/AliRezaJoodi
# Source Link:	    	https://www.w3schools.com/python/ref_string_ljust.asp
# Source Link:	   	https://www.w3schools.com/python/ref_string_rjust.asp

# The ljust() method will left align the string, using a specified character (space is default) as the fill character.
txt = "banana"
x = txt.ljust(20)
print(x, "is my favorite fruit.") 
x = txt.ljust(20, "_")
print(x) 

# The rjust() method will right align the string, using a specified character (space is default) as the fill character.
txt = "banana"
x = txt.rjust(20)
print(x, "is my favorite fruit.") 
x = txt.rjust(20, "_")
print(x)

title = "numbers (Orginal):"
description = [2, 1, 3, 5, 6, 7, 8, 9, 10, 11, 13, 14, 16]
title = title.ljust(20, " ")
print(title, description)