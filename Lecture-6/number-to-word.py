"""
123 -> "one two three" 
103 -> "one zero three" 
"""
number = input("Digit: ")
words = ""
for digit in number:
    digit = int(digit)
    match digit: 
        case 1: 
            # words = words + "one"
            words += "one"
        case 2: 
            words += "two"
        case 3: 
            words += "three"
        case 4: 
            words += "four"
        case 5: 
            words += "five"
        case 6: 
            words += "six"
        case 7: 
            words += "seven"
        case 8: 
            words += "eight"
        case 9: 
            words += "nine"
        case 0: 
            words += "zero"
    words += " "

print(words.title())