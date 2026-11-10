"""
age > 18 -> adult 
age < 18 -> minor's 
"""
age = int(input("Enter age: "))
# result = ""
# if age > 18: 
#     result = "adult"
# else: 
#     result = "minor"
result = "adult" if age > 18 else "minor"
print(result)