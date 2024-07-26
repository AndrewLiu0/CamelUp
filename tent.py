
import random
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
        self.dices = {green, yellow, red, blue, purple}
    
    # def roll 

class Dice:
    def __init__(self, name) -> None:
        self.name = name
    def getRandomNumber():
        return random.randint(1,3)