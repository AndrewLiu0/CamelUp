import unittest
from camel_up import GameState
from tent import Tent


class TestTent(unittest.TestCase):
    def setUp(self):
        self.gameState = GameState()
        self.tent = Tent()
    
    def test_0(self):
        # print("pee", self.gameState.board_camels)
        # print("peepy", self.gameState.camel_positions)
        self.gameState.movement("Red", 1)
        # print("poop", self.gameState.board_camels)
        # print("poopy", self.gameState.camel_positions)
    
if __name__ == "__main__":
    unittest.main()