# Consolidation Project #2: Tuple Out Dice Game

import random

def roll_dice():
    return [random.randint(1, 6) for _ in range(3)]

def check_tupled_out(dice_values):
    return len(set(dice_values)) == 1

