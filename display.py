from camel_up import GameState

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
    def __init__(self, camel_up:GameState):
        self.__camel_up = camel_up
    
    def game_display(self):
        print(f"Ticket Tents: {self.__camel_up.available_betting_tickets} Dice Tents: ")
        tree = '🌴'
        flag = '🏁'
        print(f"{tree} {flag}")
        print(f"{tree} {flag}")
        print(f"{tree} {flag}")
        print(f"{tree} {flag}")
        print(f"{tree} {flag}")
        print("1   2   3   4  etc")
        print(f"p1 has coins. Bets:       p2 has  coins. Bets: ")
        input = print("p1 - (B)et or (R)oll?")
        
    