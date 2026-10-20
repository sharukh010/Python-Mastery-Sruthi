"""
A code lock asks for two numbers. The lock first shows the two numbers joined side by side as
a code, and then shows their sum as a check value. Write a program that reads the two
numbers and prints both results on separate lines. Use the prompts First number: and
Second number: .
Sample Input
First number: 12
Second number: 30
Sample Output
1230
42
Explanation: the first line joins the text 12 and 30 into 1230. The second line adds the numbers
12 and 30 to get 42.
"""
first_number = input("Enter first number: ")
second_number = input("Enter second number: ")
print(first_number + second_number)
print(int(first_number)+int(second_number))

