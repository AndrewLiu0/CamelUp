#Class for Game States/Updating Game States
import random
class GameState:
    '''TODO
    
    Implement Initialization
    Implement Rolls
    Implement Bets
    Implement Scoring System


    '''
    def __init__(self):
        self.colors = ["green", "yellow", "red", "blue", "purple"]
        self.camel_positions = {}
        self.board_camels = [[]]*16
        self.available_betting_tickets = {}
        self.player_betting_tickets = [[], []]
        self.player_scores = [0, 0]
        self.taken_rolls = self.colors.copy()
        for color in self.colors:
            self.camel_positions[color] = 0
            self.available_betting_tickets[color] = [5, 3, 2, 2]
    
    def roll_dice(self, player: int):
        self.player_scores[player] += 1
    
    def bet(self, player: int, camel_color: str):
        pass
    
        


    