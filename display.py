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
    def __init__(self, tickets:dict[str, int], dice:list[int], camel_positions:dict[str, int], player_scores:list[int, int], player_betting_tickets:dict{list, list}):
        self.tickets = tickets
    
    def game_display(self):
        print(f"Ticket Tents: Dice Tents: ")
        tree = '🌴'
        flag = '🏁'
        print(f"{tree} {flag}")
        print("1   2   3   4  etc")
        print(f"p1 has x coins. Bets: 5")
        
    