# 02_pop_up_shop

def pop_up_shop():
    fruit_prices = {"apple": 1.5,"durian": 50,"jackfruit": 20,"kiwi": 2,"rambutan": 3,"mango": 8,
    }
    total_cost = 0

    for fruit, price in fruit_prices.items():
        try:
            quantity = int(input(f"How many ({fruit}) do you want?: "))
            total_cost += quantity * price
        except ValueError:
            print("Invalid input. Quantity must be a number. Skipping this fruit.")

    print(f"Your total is ${total_cost}")