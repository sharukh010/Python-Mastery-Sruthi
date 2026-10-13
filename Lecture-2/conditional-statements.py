"""
1. if 
2. elif - dependent on if 
- as many elif as possible 
3. else - dependent on if 
- one else statement for a if condition 
4. match <- later 
"""
# num = 12

# if num %2 == 0: 
#     # this statement will only gets executed when the condition is true 
#     print("Even number")
# elif num % 2 != 0: 
#     # this will not be checked if the above statement is correct 
#     print("Odd number")
# if num%2 != 0: 
#     print("Odd number")

# if num%2 == 0: 
#     print("Even number")
# else: 
#     print("Odd number")

light = input("Enter a colour (red/yellow/green): ")
if light == "red": 
    print("STOP")
elif light == "yellow": 
    print("WAIT")
elif light == "green": 
    print("GO")
else: 
    print("Invalid colour")