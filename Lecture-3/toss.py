"""
I am going to use a number to assign with the result 
1. heads 
2. tails 
now i need to generate a random number between 1 and 2 
this we are going to do it with random module 
"""
import random 

value = random.randint(1,2)
if value == 1: 
    print("Heads")
else: 
    print("Tails")