# Dice Rolling Program
from random import randint

roll_counter = 1
roll_again = True  # going to be multipurpose. Probably not recommended
dice_id = 0
dice_number = int(input("How many di are we playing with? "))

while (roll_again):
    for x in range(0, dice_number):
        print("Dice Roll ", roll_counter, ": ", "Dice_ID: ", dice_id + 1, "= ", randint(1, 6))
        dice_id += 1
    roll_counter += 1
    roll_again = str(input("Roll again? Y or N"))  # now roll_again is used as an input receiver
    if (roll_again == "Y" or roll_again == "y" or roll_again == ""):
        roll_again = True
        dice_id = 0
    else:
        print("Thanks for playing!")
        break
