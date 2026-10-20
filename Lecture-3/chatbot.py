"""
we will have questions and answers with use 
that are defined in the program 
homework: 
create a chatbot which can answer any question about 
atleast 10 questions. 
try to keep you're answers creative 
"""
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
prompt = input("Prompt: ")
if prompt == question1:
    print(f"Response: {answer1}")
elif prompt == question2: 
    print(f"Response: {answer2}")
elif prompt == question3: 
    print(f"Response: {answer3}")
elif prompt == question4:
    print(f"Response: {answer4}")
elif prompt == question5:
    print(f"Response: {answer5}")
else: 
    print("Sorry I cannot answer this question. My knowledge is limited.")