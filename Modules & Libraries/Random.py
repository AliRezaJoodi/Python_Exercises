# My GitHub:  		GitHub.com/AliRezaJoodi
from display import *
import random
import string

number = random.randrange(5,10)
display("randrange (5 to 10):", number)

number = random.randrange(10)
display("randrange (10):", number)

number = random.randint(5,10)
display("randint (5 to 10):", number)

name = ['Ali', 'Bob','Daniel', 'Hoouk', 'Starwalker']
txt_str = random.choice(name)
display("random.choice:", txt_str)
#print(type(txt_str))
txt_list = random.choices(name)
display("random.choices:", txt_list)
#print(type(txt_list))

txt_str="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
txt_list= random.sample(txt_str, 8)
display("random.sample:", txt_list)

txt_str="1234ABCDabcd"
display("txt_str  (Orginal):", txt_str)
txt_list = list(txt_str)
display("txt_list (Orginal):", txt_list)
random.shuffle(txt_list)
display("txt_list (Shuffle):", txt_list)
txt_str= "".join(txt_list)
display("txt_str  (Shuffle):", txt_str)

