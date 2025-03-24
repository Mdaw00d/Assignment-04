# 04_tall_enough_to_ride


def tall_enough_to_ride():
    MINIMUM_HEIGHT = 50
    while True:
        height_input = input("How tall are you? (Enter nothing to quit) ")
        if not height_input:
            break
        try:
            height = int(height_input)
            if height >= MINIMUM_HEIGHT:
                print("You're tall enough to ride!")
            else:
                print("You're not tall enough to ride, but maybe next year!")
        except ValueError:
            print("Invalid input. Please enter a number.")
