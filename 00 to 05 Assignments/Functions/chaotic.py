# 01_chaotic_counting
import random

DONE_LIKELIHOOD = 0.3

def chaotic_counting():
    for i in range(1, 11):
        if random.random() < DONE_LIKELIHOOD:
            print("I'm done.")
            return
        print(i)
    print("I'm done.")