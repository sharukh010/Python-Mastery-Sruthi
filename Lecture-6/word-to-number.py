"""
our goal is to get 
"one two three" -> 123 
so first we start from 
"one" -> 1 
"two" -> 2 
"one two three"-> "one","two","three" splitting a string 
"""

word = input("Number in words: ").lower()
words = word.split()
number = ""
for word in words: 
    match word: 
        case "one": 
            number += "1"
        case "two": 
            number += "2"
        case "three": 
            number += "3"
        case "four": 
            number += "4"
        case "five": 
            number += "5"
        case "six": 
            number += "6"
        case "seven": 
            number += "7"
        case "eight": 
            number += "8"
        case "nine": 
            number += "9"
        case "zero": 
            number += "0"
print(number)