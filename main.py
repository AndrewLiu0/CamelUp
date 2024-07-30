from camel_up import GameState
from display import Display
from expected_value import ExpectedValue
from colorama import *

if __name__ == "__main__":
    gameState = GameState()
    display = Display(gameState)
    display.game_display(gameState)
    turn = 0
    while len(gameState.tent.dices) > 0:
        move = ""
        while move != "b" and move != "r":
            if turn % 2 == 0:
                move = input("p1 - (B)et or (R)oll? ")
                move = move.lower()
                print()
            else:
                move = input("p2 - (B)et or (R)oll? ")
                move = move.lower()
                print()
        # add possibilities here
        enumerative = ExpectedValue(gameState).calculate()
        print(enumerative)

        # (possibilities[key])[0] = round((possibilities[key])[0], 2)
        # (possibilities[key])[1] = round((possibilities[key])[1], 2)

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
            ans += + "  " + (enumerative[camel])[0] + "  " + (enumerative[camel])[1]
            print(ans)

        if move == "r":
            roll = gameState.tent.roll()
            gameState.movement(roll[0], roll[1])
            gameState.player_scores[turn % 2] += 1
        else:
            bet = ""
            length = 1
            while True:
                bet = input("What color do you want to bet on? ")
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
        display.game_display(gameState)
        turn += 1
    scores = gameState.pay_out()
    first = "🥇"
    second = "🥈"
    print()
    if scores[0] > scores[1]:
        print(f"p1 comes in 1st with {scores[0]} coins {first} {first} {first}!")
        print(f"p2 comes in 2nd with {scores[1]} coins {second} {second} {second}!")
    elif scores[1] > scores[0]:
        print(f"p2 comes in 1st with {scores[1]} coins {first} {first} {first}!")
        print(f"p1 comes in 2nd with {scores[0]} coins {second} {second} {second}!")
    else:
        print(f"p1 and p2 tie {first} {first} {first}!")