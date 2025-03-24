# 03_wholesome_machine
def wholesome_machine():
    affirmation = "I am capable of doing anything I put my mind to."

    while True:
        user_input = input(f"Please type the following affirmation: {affirmation} ")
        if user_input == affirmation:
            print("That's right! :)")
            break
        else:
            print("Hmmm That was not the affirmation.") 