#this program asks the user for how many dice and how many sides

import random

# dice class
class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)

def get_integer_input(user_input):
    while True:
        try:
            user_int = int(input(user_input))
            return user_int
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

print("How many dice would you like to roll?")
num_dice = get_integer_input("Enter the number of dice: ")

print("How many sides would you like each dice to have?")
dice_sides = get_integer_input("Enter the number of sides for each dice: ")

# Create a list of Dice objects
dice_list = [Dice(sides=dice_sides) for _ in range(num_dice)]

# Roll each dice and print the result
dice_total = 0
for die in dice_list:
    result = die.roll()
    print(f"The result of rolling a {die.sides}-sided die is: {result}")
    dice_total = dice_total + result
print(f"The total is: {dice_total}")
