import unittest
from src.Laberinth import Laberinth


class LaberinthTest(unittest.TestCase):

    def setUp(self):
        self.laberinth = Laberinth(3, 7)
        self.laberinth.obstacles = [(0, 1), (2, 0), (2, 5)]
        self.laberinth.targets = [(2, 6), (0, 6), (2, 4)]

    def test_laberinth_rows(self):
        self.assertEqual(3, len(self.laberinth.laberinth))

    def test_laberinth_columns(self):
        self.assertEqual(7, len(self.laberinth.laberinth[0]))
        self.assertEqual(7, len(self.laberinth.laberinth[1]))
        self.assertEqual(7, len(self.laberinth.laberinth[2]))

    def test_is_valid_position(self):
        self.assertTrue(self.laberinth.is_valid_position(0, 2))
        self.assertFalse(self.laberinth.is_valid_position(0, 1))
        self.assertTrue(self.laberinth.is_valid_position(0, 0))
        self.assertTrue(self.laberinth.is_valid_position(1, 6))
        self.assertTrue(self.laberinth.is_valid_position(1, 3))
        self.assertTrue(self.laberinth.is_valid_position(1, 1))
        self.assertFalse(self.laberinth.is_valid_position(3, 2))
        self.assertFalse(self.laberinth.is_valid_position(3, 1))
        self.assertFalse(self.laberinth.is_valid_position(3, 0))
        self.assertFalse(self.laberinth.is_valid_position(4, 7))
        self.assertFalse(self.laberinth.is_valid_position(-1, 0))
        self.assertFalse(self.laberinth.is_valid_position(1, -1))
        self.assertTrue(self.laberinth.is_valid_position(2, 4))
