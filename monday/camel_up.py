#Class for Game States/Updating Game States
import random
from tent import Tent
from colorama import *
init(autoreset=True)

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
        self.board_camels = []
        for i in range(16):
            self.board_camels.append([])
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
        self.inital_tent = Tent()
        self.tent = Tent()
        #We are initializing the camel positions.
        self.initial_rolls = []
        for i in range(5):
            self.initial_rolls.append(self.inital_tent.roll())
        for roll in self.initial_rolls:
            self.camel_positions[roll[0]] = roll[1]
            self.available_betting_tickets[roll[0]] = [5, 3, 2, 2]
            
        for color in self.camel_positions:
            #print("positions", self.camel_positions)
            self.board_camels[self.camel_positions[color]].append(color)
    
    # def roll_dice(self, player: int) -> tuple():
    #     self.player_scores[player] += 1
    #     camel_color = random.choice(self.taken_rolls)
    #     self.taken_rolls.remove(camel_color)
    
    def ticketTentsString(self):
        ans = ""
        for ticket in self.available_betting_tickets:
            if ticket == "Green":
                if len(ticket) > 0:
                    ans += Back.GREEN + str((self.available_betting_tickets[ticket])[0])
                else:
                    ans += Back.GREEN + "X"
            elif ticket == "Yellow":
                if len(ticket) > 0:
                    ans += Back.YELLOW + str((self.available_betting_tickets[ticket])[0])
                else:
                    ans += Back.YELLOW + "X"
            elif ticket == "Red":
                if len(ticket) > 0:
                    ans += Back.RED + str((self.available_betting_tickets[ticket])[0])
                else:
                    ans += Back.RED + "X"
            elif ticket == "Blue":
                if len(ticket) > 0:
                    ans += Back.BLUE + str((self.available_betting_tickets[ticket])[0])
                else:
                    ans += Back.BLUE + "X"
            elif ticket == "Purple":
                if len(ticket) > 0:
                    ans += Back.MAGENTA + str((self.available_betting_tickets[ticket])[0])
                else:
                    ans += Back.MAGENTA + "X"
            ans += Style.RESET_ALL + " "
        return ans + Style.RESET_ALL
    
    def movement(self, camel: str, move_number: int):
        '''This moves stuff. I have no idea if this is right.
        Ideally this is what the code does:
        It takes the current camel and all the camels on top of the current camel
        and then it moves all of them by the move number.
        And then it updates their positions.
        '''
        old_position = self.camel_positions[camel]
        # print("camels", self.board_camels)
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
        


    