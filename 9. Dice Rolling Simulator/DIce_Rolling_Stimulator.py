import random


def RollDice(Dices, Sides):
    total = 0
    rolls = []
    for i in range(Dices):
        roll = random.randint(1, Sides)
        total += roll
        rolls.append(roll)

    return rolls, total


Dices = int(input("Enter the number of dices: "))
Sides = int(input("Enter the number of sides for each dice: "))

rolls, total = RollDice(Dices, Sides)

print(f"You rolled {Dices} dice with {Sides} sides each.")
print(f"The total is {total}.")
print(f"The individual rolls are {rolls}.")
