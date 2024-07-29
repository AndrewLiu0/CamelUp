#Class for Game States/Updating Game States
import random
from tent import Tent

class GameState:
    '''TODO
    
    Implement Initialization
    Implement Rolls
    Implement Bets
    Implement Scoring System


    '''
    def __init__(self):
        #This tells me the types of colors the camels can have.
        self.colors = ["Green", "Yellow", "Red", "Blue", "Purple"]
        #This tells me the position each camel is at.
        self.camel_positions = {}
        #This tells me what the board looks like.
        self.board_camels = [[]]*16
        #These are the available betting tickets for each camel.
        self.available_betting_tickets = {}
        #These are the betting tickets each player has.
        self.player_betting_tickets = [[], []]
        #These are the player scores.
        self.player_scores = [0, 0]
        #These are the camels that still can roll.
        self.taken_rolls = self.colors.copy()
        self.rolls = []
        #I have no idea what the heck this is. Andrew and Christina will do this.
        self.tent = Tent()
        #We are initializing the camel positions.
        for color in self.colors:
            self.camel_positions[color] = 0
            self.available_betting_tickets[color] = [5, 3, 2, 2]
    
    # def roll_dice(self, player: int) -> tuple():
    #     self.player_scores[player] += 1
    #     camel_color = random.choice(self.taken_rolls)
    #     self.taken_rolls.remove(camel_color)
    
    def movement(self, camel: str, move_number: int):
        '''This moves stuff. I have no idea if this is right.
        Ideally this is what the code does:
        It takes the current camel and all the camels on top of the current camel
        and then it moves all of them by the move number.
        And then it updates their positions.
        '''
        old_position = self.camel_positions[camel]
        camels_on_top = self.board_camels[old_position][self.board_camels[old_position].index(camel):].copy()
        next_position = old_position + move_number
        self.board_camels[next_position].extend(camels_on_top)
        for animal in camels_on_top:
            self.board_camels[old_position].remove(animal)
        for animal in camels_on_top:
            self.camel_positions[animal] = next_position

    def bet(self, player: int, camel_color: str) -> bool:
        '''
        Bet takes in two parameters: the player who bets, and the camel the player is betting on.
        Bet updates the gamestate to reflect the bet (e.g. modifies our betting ticket lists).
        Bet returns True if the GameState was successfully updated. Otherwise, it returns false.
        '''
        betting_tickets = self.player_betting_tickets[player]
        available_tickets = self.available_betting_tickets[camel_color]
        print(available_tickets)
        if(available_tickets):
            ticket = available_tickets.pop(0)
            print(available_tickets)
            betting_tickets.append(ticket)
            return True
        return False
        

    def pay_out(self):
        pass
        


    