from random import randint # randint 
# import random # random.randint() 

# Defining constants 
ROCK = 1 
PAPER = 2 
SCISSORS = 3 

program_number = randint(1,3)
options = """Options: 
1. Rock 
2. Paper 
3. Scissors"""
print(options)
user_number = int(input("Enter your choice (1-3): "))

if user_number <= 0 or user_number > 3: 
    user_number = ROCK 

program_choice = "" 
user_choice = "" 

if program_number == ROCK:
    program_choice = "ROCK"
elif program_number == PAPER: 
    program_choice = "PAPER"
elif program_number  == SCISSORS: 
    program_choice = "SCISSORS" 

if user_number == ROCK: 
    user_choice = "ROCK"
elif user_number == PAPER: 
    user_choice = "PAPER"
elif user_number == SCISSORS: 
    user_choice = "SCISSORS"

print(f"Program Choice: {program_choice}")
print(f"User Choice: {user_choice}")

print("Verdict: ")
if program_number == ROCK and user_number == PAPER: 
    print("User Won..")
elif program_number == ROCK and user_number == SCISSORS: 
    print("Program Won..")
elif program_number == PAPER and user_number == ROCK: 
    print("Program Won..")
elif program_number == PAPER and user_number == SCISSORS: 
    print("User Won..")
elif program_number == SCISSORS and user_number == ROCK: 
    print("User Won..")
elif program_number == SCISSORS and user_number == PAPER: 
    print("Program Won..")
else: 
    print("It's a Tie..")

