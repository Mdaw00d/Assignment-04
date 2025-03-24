# 04_pythagorean_theorem

import math  

def pythagorean_theorem():
    base = float(input("Enter the length of base: "))
    perpendicular = float(input("Enter the length of perpendicular: "))
    return math.sqrt((perpendicular**2) * (base**2))
