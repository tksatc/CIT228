from random import randint

#-----------------------Extra-Credit - Exercise 9-13------------------------

class Die:
    """Represents an n-sided die"""
    def __init__(self, sides=6):
        """Initializes the die attribute"""
        self.sides = sides
    
    def roll_die(self):
        """Displays the results of a roll of the die"""
        roll = randint(1, self.sides)
        print(f"You have rolled a: {roll}")


die1 = Die()
die2 = Die(10)
die3 = Die(20)

dice = [die1, die2, die3]

maxRolls = 10

for die in dice:
    totalRolls = 0
    print(f"\n{die.sides}-sided die rolled the following: ")
    print("---------------------------------")

    while totalRolls < maxRolls:
          die.roll_die()
          totalRolls += 1
          
    print(f"\n{die.sides}-sided die was rolled {totalRolls} times.\n")
