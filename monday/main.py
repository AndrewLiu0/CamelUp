from camel_up import GameState
from display import Display

if __name__ == "__main__":
    gameState = GameState()
    display = Display(gameState)
    display.game_display()