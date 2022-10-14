# My GitHub:  		GitHub.com/AliRezaJoodi

import random

number = random.randrange(5,10)
print("randrange (5 to 10):", number)

number = random.randrange(10)
print("randrange (10):", number)

number = random.randint(5,10)
print("randint (5 to 10):", number)

name = ['Ali', 'Bob','Daniel', 'Hoouk', 'Starwalker']
txt_str = random.choice(name)
print("random.choice:", txt_str)
#print(type(txt_str))

txt_list = random.choices(name)
print("random.choices:", txt_list)
#print(type(txt_list))

txt="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
print("random.sample:", random.sample(txt,8))