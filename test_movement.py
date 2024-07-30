import unittest
from camel_up import GameState
from tent import Tent
from display import Display


class TestTent(unittest.TestCase):
    def setUp(self):
        self.gameState = GameState()
        self.display = Display(self.gameState)
    
    def test_0(self):
        # print("pee", self.gameState.board_camels)
        # print("peepy", self.gameState.camel_positions)
        Display(self.gameState).game_display()
        self.gameState.movement("Red", 1)
        Display(self.gameState).game_display()
        # print("poop", self.gameState.board_camels)
        # print("poopy", self.gameState.camel_positions)
    
if __name__ == "__main__":
    unittest.main()