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
        self.__colors = ["green", "yellow", "red", "blue", "purple"]
        self.__camel_positions = {}
        self.__board_camels = [[]]*16
        self.__available_betting_tickets = {}
        self.__player_betting_tickets = [[], []]
        self.__player_scores = [0, 0]
        self.__taken_rolls = self.__colors.copy()
        for color in self.__colors:
            self.__camel_positions[color] = 0
            self.__available_betting_tickets[color] = [5, 3, 2, 2]
        
    @property
    def camel_positions(self):
        return self.__camel_positions
    
    @property
    def board_camels(self):
        return self.__board_camels
    
    @property
    def available_betting_tickets(self):
        return self.__available_betting_tickets
    
    @property
    def player_betting_tickets(self):
        return self.__player_betting_tickets
    
    @property
    def player_scores(self):
        return self.__player_scores
    
    @property
    def taken_rolls(self):
        return self.__taken_rolls
    
    def roll_dice(self, player: int):
        self.__player_scores[player] += 1
    
    def bet(self, player: int, camel_color: str):
        pass

    def pay_out(self):
        pass
        


    