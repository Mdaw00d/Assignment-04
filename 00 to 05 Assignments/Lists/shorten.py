# 08_shorten

max_length = 3
def shorten_and_print(lst):
    """Removes elements from the end of lst until it reaches MAX_LENGTH and prints them."""
    while len(lst) > max_length:
        print(lst.pop())
    print("Shortened list:", lst)

# Example usage:
my_list = input("Enter a list of items separated by spaces: ").split()
shorten_and_print(my_list)