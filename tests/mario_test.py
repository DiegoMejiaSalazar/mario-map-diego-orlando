import unittest
from src.Laberinth import Laberinth
from src.Agent import Agent


class MarioTest(unittest.TestCase):

    def setUp(self):
        laberinth = Laberinth(9, 11)
        laberinth.obstacles = [(0, 1), (2, 0), (2, 3)]
        laberinth.targets = [(0, 3), (1, 3)]
        self.mario = Agent()
        self.mario.x_position = 0
        self.mario.y_position = 0
        self.mario.set_laberinth(laberinth)

    def test_astar_search(self):
        self.mario.laberinth.show()
        print("*" * 50)
        self.mario.manhattan_distance()
        print(self.mario.astar())