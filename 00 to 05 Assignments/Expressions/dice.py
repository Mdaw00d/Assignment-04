# 01_dicesimulator
import random
def roll_dice():
    total_slides=6
    dice1 = random.randint(1,total_slides)
    dice2 = random.randint(1,total_slides)
    print(dice1+dice2)

def roll_stimulator():
    roll_dice()
    roll_dice()