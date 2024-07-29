from camel_up import GameState
from tent import *
from colorama import *

class Display:
    '''
    Playing state
    End game state
    Ticket Tents: betting card at the top
    Dice Tents: what dice was last rolled
    Display of where camels are
    p1 has x coins. Bets: y
    p1 - (B)et or (R)oll?
    '''
    def __init__(self, gameState:GameState):
        self.__camel_up = GameState()
    
    def game_display(self):
        Style.RESET_ALL
        print(f"Ticket Tents: {self.__camel_up.ticketTentsString()} Dice Tents: {self.__camel_up.tent}")
        tree = '🌴'
        flag = '🏁'
        print(f"{tree} {flag}")
        print(f"{tree} {flag}")
        print(f"{tree} {flag}")
        print(f"{tree} {flag}")
        print(f"{tree} {flag}")
        print("1   2   3   4  etc")
        print(f"p1 has {self.__camel_up.player_scores[0]} coins. Bets: {self.__camel_up.player_betting_tickets[0]}  \np2 has {self.__camel_up.player_scores[1]} coins. Bets: {self.__camel_up.player_betting_tickets[1]}")
        input = print("p1 - (B)et or (R)oll?")
        # while True:
        #     if input == "B":
        #         break
        #     elif input == "R":
        #         break
        #     else:
        #         print("You have an invalid input. Try again.")
        #         input = print("p1 - (B)et or (R)oll?")
    
        
    