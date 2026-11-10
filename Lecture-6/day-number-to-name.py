number = int(input("Enter a Number (1-7): "))
day = ""
match number: 
    case 1: 
        # this will be executed when number value is 1 
        day = "monday"
    case 2: 
        day = "tuesday"
    case 3: 
        day = "wednesday"
    case 4: 
        day = "thursday"
    case 5: 
        day = "friday"
    case 6: 
        day = "saturday"
    case 7: 
        day = "sunday"
    case _: # default case 
        print("Invalid day number. Try again")

print(day)