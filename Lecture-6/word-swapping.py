"""
sit -> stand 
stand -> sit 
sitting -> standing 
standing -> sitting 
happy -> sad 
sad -> happy
like -> hate 
hate -> like 
day -> night 
night -> day 
eat -> drink 
drink -> eat 
eating -> drinking 
drinking -> eating 

"""
sentence = input("Sentence: ").lower() 
words = sentence.split()
final_sentence = ""
for word in words: 
    match word: 
        case "eat": 
            final_sentence += "drink"
        case "drink": 
            final_sentence += "eat"
        case "eating": 
            final_sentence += "drinking"
        case "drinking": 
            final_sentence += "eating"
        case "day": 
            final_sentence += "night"
        case "night": 
            final_sentence += "day"
        case "sad": 
            final_sentence += "happy"
        case "happy": 
            final_sentence += "sad"
        case "hate": 
            final_sentence += "like"
        case "like": 
            final_sentence += "hate"
        case _ : 
            final_sentence += word
    final_sentence += " "
print(final_sentence.title())