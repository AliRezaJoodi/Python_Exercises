# GitHub.com/AliRezaJoodi

import random

number = random.randrange(5,10)
print("Random Number (5 to 10): ", number)

number = random.randrange(10)
print("Random Number (0 to 10): ", number)

number = random.randint(5,10)
print("Random Number (5 to 10): ", number)

name = ['Ali', 'Bob','Daniel', 'Hoouk', 'Starwalker']
print("Random Name: ", random.choice(name))

txt="!#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
print("Password Generator: ", random.sample(txt,8))