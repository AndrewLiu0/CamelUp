# make a list of all possible dice rolls
# make a copy of gamestate
# play out all the moves
# keep track of who is first, second, third, etc
# divide how many times first, second by the number of possibilities
from camel_up import GameState
from display import *
from tent import Dice
from copy import deepcopy
import itertools
import math

class ExpectedValue():
    def __init__(self, gameState:GameState):
        self.gameState = gameState
        self.possibilities = None
    
    
    def calculate(self) -> dict[str, list[float]]:
        '''
        Returns a dictionary
        Key: Camel Color
        Value: List of Probability of Camel coming in nth + 1 place where n is the index of the list
        Ex: Purple: [1/2, 1/3, 1/6, 0, 0]
        
        '''
        gameState = deepcopy(self.gameState)
        #dice is an array of strings i.e. ['purple', 'yellow']
        dice = []
        for die in gameState.tent.dices:
            dice.append(die.name)
        color_hash = {"green": 1, "yellow": 2, "red": 3, "blue": 4, "purple": 5}

        #print(f'Color Hash: {color_hash}')
        possibilities = {"green": [0.00, 0.00], "yellow": [0.00, 0.00], "red": [0.00, 0.00], "blue": [0.00, 0.00], "purple": [0.00, 0.00]}
        for process in itertools.permutations(dice):
            for i in range(243, 486, 1):
                gameState2 = deepcopy(gameState)
                minus_one_camel_moves = self.ternary(i)
                for camel in process:
                    current_move = int(minus_one_camel_moves[color_hash[camel]]) + 1
                    gameState2.movement(camel, current_move)
                placements = self.probability(gameState2)
                possibilities[placements[0]][0] += 1.00
                possibilities[placements[1]][1] += 1.00
        for key in possibilities:
            (possibilities[key])[0] /= math.factorial(len(dice)) * pow(3, 5)
            (possibilities[key])[1] /= math.factorial(len(dice)) * pow(3, 5)
            # (possibilities[key])[0] = round((possibilities[key])[0], 2)
            # (possibilities[key])[1] = round((possibilities[key])[1], 2)

        self.possibilities = possibilities
        return possibilities
    
    
    def calculateEv(self, camel: str, possibilities):
        pFirst = possibilities[camel][0]
        pSecond = possibilities[camel][1]
        if len(self.gameState.available_betting_tickets[camel]) == 0:
            return 0 - math.inf
        return self.gameState.available_betting_tickets[camel][0] * pFirst + 1 * pSecond  - 1 * (1 - pFirst - pSecond)
    
    
    def ternary(self, n):
        if n == 0:
            return '0'
        nums = []
        while n:
            n, r = divmod(n, 3)
            nums.append(str(r))
        return ''.join(reversed(nums))


    
    def probability(self, gameState:GameState) -> list[str]:
        # returns a list in order of first, second, third, etc
        first = ""
        second = ""
        third = ""
        fourth = ""
        fifth = ""
        for i in range(len(gameState.board_camels) - 1, 0, -1):
            while len(gameState.board_camels[i]) > 0:
                if first == "":
                    first = gameState.board_camels[i].pop()
                elif second == "":
                    second = gameState.board_camels[i].pop()
                elif third == "":
                    third = gameState.board_camels[i].pop()
                elif fourth == "":
                    fourth = gameState.board_camels[i].pop()
                elif fifth == "":
                    fifth = gameState.board_camels[i].pop()
            if first != "" and second != "" and third != "" and fourth != "" and fifth != "":
                break
        placements = [first, second, third, fourth, fifth]
        return placements
    
# gameState = GameState()
# gameState.board_camels = [[], ["red", "blue"], [], ["purple", "green"], ["yellow"], [], [], [], [], [], [], [], [], [], [], []]
# gameState.camel_positions = {"blue": 1, "red": 1, "green": 3, "purple": 3, "yellow": 4}
# gameState.tent.dices = [Dice("blue")]
# gameState.tent.rolls = [Dice("red", 1), Dice("purple", 2), Dice("yellow", 3), Dice("green", 2)]
# ev = ExpectedValue(gameState)
# display = Display(gameState)
# display.game_display(gameState)
# print(ev.calculate())
# print(ev.calculateEv("yellow"))