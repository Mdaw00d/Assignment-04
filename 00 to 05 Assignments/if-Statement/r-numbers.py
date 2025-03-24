# 05_random_numbers
import random
def random_numbers():
    for i in range(10):
        print(f"{i+1}: {random.randint(1, 100)}")
# random_numbers()