# 06_rolldice
import random


def rolldice():
    total_sides = 6
    dice1= random.randint(1,total_sides)
    dice2= random.randint(1,total_sides)
    total = dice1+dice2

    print(f"Dice 1 : {dice1}")
    print(f"Dice 2 : {dice2}")
    print(f"Total : {total}")