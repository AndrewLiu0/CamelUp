
import random
from colorama import *
init(autoreset=True)

'''
Used if player chooses to roll the dice
'''
class Tent:
    def __init__(self) -> None:
        green = Dice("Green")
        yellow = Dice("Yellow")
        red = Dice("Red")
        blue = Dice("Blue")
        purple = Dice("Purple")
        self.dices = [green, yellow, red, blue, purple]
        self.rolls = []
    
    # def roll 
    def roll(self):
        dice = random.choice(self.dices)
        color = dice.name
        roll = dice.getRandomNumber()
        self.dices.remove(dice)
        self.rolls.append(dice)
        return (color, roll)

    def __str__(self):
        ans = ""
        for dice in self.rolls:
            if dice.name == "Green":
                ans += Back.GREEN + str(dice.number)
            elif dice.name == "Yellow":
                ans += Back.YELLOW + str(dice.number)
            elif dice.name == "Red":
                ans += Back.RED + str(dice.number)
            elif dice.name == "Blue":
                ans += Back.BLUE + str(dice.number)
            elif dice.name == "Purple":
                ans += Back.MAGENTA + str(dice.number)
        return ans

class Dice:
    def __init__(self, name) -> None:
        self.name = name
        self.number = None
    def getRandomNumber(self):
        value = random.randint(1,3)
        self.number = value
        return value