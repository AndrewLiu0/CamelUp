from camel_up import GameState
from display import Display
from expected_value import ExpectedValue
from colorama import *
import math
from copy import deepcopy

def ai_advice(gameState:GameState):
    enumerative = ExpectedValue(gameState).calculate()
    print("AI Advice-")
    print("   1st   2nd")

    for camel in enumerative:
        if camel == "green":
            ans = Back.GREEN + "g" + Style.RESET_ALL
        elif camel == "blue":
            ans = Back.BLUE + "b" + Style.RESET_ALL
        elif camel == "yellow":
            ans = Back.YELLOW + "y" + Style.RESET_ALL
        elif camel == "purple":
            ans = Back.MAGENTA + "p" + Style.RESET_ALL
        elif camel == "red":
            ans = Back.RED + "r" + Style.RESET_ALL
        first = round((enumerative[camel])[0], 2)
        second = round((enumerative[camel])[1], 2)
        ans += "  %3.2f" %(first)
        ans += "  %3.2f" %(second)
        print(ans)
    
    ans = "Available betting tickets:"
    
    evs = {}
    
    max_ev = -1 * math.inf
    
    for camel in enumerative:
        if len(gameState.available_betting_tickets[camel]) > 0:
            ev = round(ExpectedValue(gameState).calculateEv(camel, enumerative), 2)
            evs[camel] = ev
            if ev > max_ev:
                max_ev = ev
            
    for camel in evs:
        if camel == "green":
            ans += " (g)" + Back.GREEN
        elif camel == "blue":
            ans += " (b)" + Back.BLUE
        elif camel == "yellow":
            ans += " (y)" + Back.YELLOW
        elif camel == "purple":
            ans += " (p)" + Back.MAGENTA
        elif camel == "red":
            ans += " (r)" + Back.RED
        ans += str(gameState.available_betting_tickets[camel][0]) + Style.RESET_ALL
        if evs[camel] == max_ev and max_ev >= 1:
            ans += " " + Fore.GREEN + Back.WHITE + "EV:%.2f" %(evs[camel]) + Style.RESET_ALL
        else:
            ans += " EV:%.2f" %(evs[camel])
        
    print(ans)
    print()
    
def placements(gameState:GameState) -> list[str]:
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

if __name__ == "__main__":
    leg = 1
    p1 = 0
    p2 = 0
    mode = input("Do you want auto AI advice? (y/n) ")
    print()
    starting_positions = {}
    board_positions = []
    end = False
    
    while not end:
        gameState = GameState()
        if leg > 1:
            gameState.camel_positions = deepcopy(starting_positions)
            gameState.board_camels = deepcopy(board_positions)
        display = Display(gameState)
        print()
        display.game_display(gameState)
        turn = 0
        while len(gameState.tent.dices) > 0:
            if mode == "y":
                ai_advice(gameState)
            restart = False
            move = ""
            while move != "b" and move != "r" and move != "t":
                if turn % 2 == 0:
                    move = input("p1 - (T)icket or (R)oll or (B)et? ")
                    move = move.lower()
                    print()
                else:
                    move = input("p2 - (T)icket or (R)oll or (B)et? ")
                    move = move.lower()
                    print()

            if move == "r":
                roll = gameState.tent.roll()
                if not gameState.movement(roll[0], roll[1]):
                    end = True
                    break
                gameState.player_scores[turn % 2] += 1
            elif move == "t":
                if mode == "n":
                    ai_advice(gameState)
                bet = ""
                length = 1
                while True:
                    bet = input("What color do you want to bet on or (n) to not bet. ")
                    if bet == "n":
                        restart = True
                        break
                    if bet in gameState.colors or bet in gameState.colors_short:
                        if bet == "g":
                            bet = "green"
                        elif bet == "y":
                            bet = "yellow"
                        elif bet == "p":
                            bet = "purple"
                        elif bet == "b":
                            bet = "blue"
                        elif bet == "r":
                            bet = "red"
                        if gameState.bet(turn % 2, bet):
                            break
                    print()
            elif move == "b":
                camel_color = ""
                pos = ""
                while True:
                    bet = input("Which camel do you want to bet on and winner or loser? (color, w/l) ")
                    camel_color = bet.split(",")[0].strip()
                    pos = bet.split(",")[1].strip()
                    if camel_color == "g":
                        camel_color = "green"
                    elif camel_color == "y":
                        camel_color = "yellow"
                    elif camel_color == "p":
                        camel_color = "purple"
                    elif camel_color == "b":
                        camel_color = "blue"
                    elif camel_color == "r":
                        camel_color = "red"
                    if pos == "w":
                        pos = 0
                    elif pos == "l":
                        pos = 1
                    move = (turn % 2, camel_color)
                    if pos == 0:
                        if move not in gameState.overall_winner and camel_color in gameState.colors:
                            break
                    elif pos == 1:
                        if move not in gameState.overall_loser and camel_color in gameState.colors:
                            break
                gameState.overall(turn % 2, camel_color, pos)
            if not restart:
                print("---------------------------------------------------------------------------------")
                display.game_display(gameState)
                turn += 1
            starting_positions = deepcopy(gameState.camel_positions)
            board_positions = deepcopy(gameState.board_camels)
        finalGameState = deepcopy(gameState)
        scores = gameState.pay_out()
        p1 += scores[0]
        p2 += scores[1]
        first = "🥇"
        second = "🥈"
        print()
        print(f"Leg {leg} scores: ")
        if scores[0] > scores[1]:
            print(f"p1 comes in 1st with {scores[0]} coins {first} {first} {first}!")
            print(f"p2 comes in 2nd with {scores[1]} coins {second} {second} {second}!")
        elif scores[1] > scores[0]:
            print(f"p2 comes in 1st with {scores[1]} coins {first} {first} {first}!")
            print(f"p1 comes in 2nd with {scores[0]} coins {second} {second} {second}!")
        else:
            print(f"p1 and p2 tie with {scores[0]} coins each {first} {first} {first}!")
        leg += 1
        print("---------------------------------------------------------------------------------")
    end = placements(finalGameState)
    for index in range(len(finalGameState.overall_winner)):
        if finalGameState.overall_winner[index][1] == end[0]:
            if finalGameState.overall_winner[index][0] == 0:
                if index == 0:
                    p1 += 8
                elif index == 1:
                    p1 += 5
                elif index == 2:
                    p1 += 3
                elif index == 3:
                    p1 += 2
                else:
                    p1 += 1
            else:
                if index == 0:
                    p2 += 8
                elif index == 1:
                    p2 += 5
                elif index == 2:
                    p2 += 3
                elif index == 3:
                    p2 += 2
                else:
                    p2 += 1
        else:
            if finalGameState.overall_winner[index][0] == 0:
                p1 -= 1
            else:
                p2 -= 1
            
    for index in range(len(finalGameState.overall_loser)):
        if finalGameState.overall_loser[index][1] == end[len(end) - 1]:
            if finalGameState.overall_loser[index][0] == 0:
                if index == 0:
                    p1 += 8
                elif index == 1:
                    p1 += 5
                elif index == 2:
                    p1 += 3
                elif index == 3:
                    p1 += 2
                else:
                    p1 += 1
            else:
                if index == 0:
                    p2 += 8
                elif index == 1:
                    p2 += 5
                elif index == 2:
                    p2 += 3
                elif index == 3:
                    p2 += 2
                else:
                    p2 += 1
        else:
            if finalGameState.overall_loser[index][0] == 0:
                p1 -= 1
            else:
                p2 -= 1
    print()
    print("Overall scores: ")
    if p1 > p2:
        print(f"p1 comes in 1st with {p1} coins {first} {first} {first}")
        print(f"p2 comes in 2nd with {p2} coins {second} {second} {second}")
    else:
        print(f"p2 comes in 1st with {p2} coins {first} {first} {first}")
        print(f"p1 comes in 2nd with {p1} coins {second} {second} {second}")