# 00_joke_bot

def joke_bot():
    prompt_message= "What do you want? "
    joke_message = "Here is a joke for you! Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'"
    sorry_message = "Sorry I only tell jokes."

    user_input = input("Enter the message: ")
    
    if "joke" in user_input.lower():
        print(joke_message)
    else:
        print(sorry_message)
