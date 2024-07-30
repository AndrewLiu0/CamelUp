from camel_up import GameState
from display import Display

if __name__ == "__main__":
    gameState = GameState()
    display = Display(gameState)
    display.game_display(gameState)
    turn = 0
    while len(gameState.tent.dices) > 0:
        move = ""
        while move != "B" and move != "R":
            if turn % 2 == 0:
                move = input("p1 - (B)et or (R)oll? ")
                print()
            else:
                move = input("p2 - (B)et or (R)oll? ")
                print()
        if move == "R":
            roll = gameState.tent.roll()
            gameState.movement(roll[0], roll[1])
            gameState.player_scores[turn % 2] += 1
        else:
            bet = ""
            length = 1
            while True:
                bet = input("What color do you want to bet on? ")
                if bet in gameState.colors:
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