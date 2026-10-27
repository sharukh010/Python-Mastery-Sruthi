question1 = "What is the result of 1+1?"
question2 = "Who own chrome browser?"
question3 = "What is the latest Iphone in the market?"
question4 = "Who is the olmpyic champion for swimming in 2026?"
question5 = "Who own tesla car company?"
answer1 = "It is 2."
answer2 = "Google owns the chrome browser."
answer3 = "Iphone 18 Pro is the new Iphone in the market."
answer4 = "It is Léon Marchand won olympic medal in 2024."
answer5 = "Elon Musk own tesla car company."
"""
1. take an umbrella whenever its raining 
- there is a chance this statement can be wrong 
2. go to school whenever the sun rises on east 
- there is no chance this statement can be wrong 
- this is an example of infite loop 
"""
while True: # infinite loop 
    prompt = input("Prompt: ")
    if prompt.lower().replace(" ","") in question1.lower().replace(" ",""):
        print(f"Response: {answer1}")
    elif prompt.lower().replace(" ","") in question2.lower().replace(" ",""): 
        print(f"Response: {answer2}")
    elif prompt.lower().replace(" ","") in question3.lower().replace(" ",""): 
        print(f"Response: {answer3}")
    elif prompt.lower().replace(" ","") in question4.lower().replace(" ",""):
        print(f"Response: {answer4}")
    elif prompt.lower().replace(" ","") in question5.lower().replace(" ",""):
        print(f"Response: {answer5}")
    else: 
        print("Sorry I cannot answer this question. My knowledge is limited.")