# 03_in_stock

def in_stock(fruit):
    """Returns the number of a given fruit in Sophia's inventory."""
    inventory = {
        "apple": 50,
        "banana": 200,
        "pear": 1000,
        "orange": 75,
    }
    return inventory.get(fruit, 0)

def in_stock_main():
    """Gets fruit input and prints stock information."""
    fruit = input("Enter a fruit: ")
    stock = in_stock(fruit)

    if stock > 0:
        print("This fruit is in stock! Here is how many:")
        print(stock)
    else:
        print("This fruit is not in stock.")

in_stock_main()