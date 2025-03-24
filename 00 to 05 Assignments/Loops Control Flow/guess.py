# 00_guess_my_number
import random
def guess_my_number():
    real_num = random.randint(0, 99)
    while True:
        try:
            user_number = int(input("Guess a number between 0 and 99: "))
            if user_number == real_num:
                print("Congratulations, you guessed the number correctly!")
                break
            elif user_number < real_num:
                print("Your guess is too low. Try again!")
            else:
                print("Your guess is too high. Try again!")
        except ValueError:
            print("Invalid input. Please enter a number.")
            break