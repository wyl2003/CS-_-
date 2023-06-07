#
# File: tons_test.py
# Descrition: test for the game
# Author: Yile Wang (王以乐)
# Student ID: 2218040121
# This is my own work as defined by 
#  the University's Academic Misconduct Policy.
#

from tons import *
import unittest


class TestGame(unittest.TestCase):

    def test_init(self):
        game = Game()


    def test_throw(self):
        game = Game()
        game.addDice(3)
        dice = game.throw()
        self.assertIn(dice[0], [1, 2, 3, 4, 5, 6])
        self.assertIn(dice[1], [1, 2, 3, 4, 5, 6])
        self.assertIn(dice[2], [1, 2, 3, 4, 5, 6])

    def test_dice(self):
        dice = Dice()
        for i in range(5):
            dice.throw(i)
            self.assertIn(dice.get_result(), [1, 2, 3, 4, 5, 6])

    def test_player(self):
        man = Player('test')
        man.add_coins(100)
        man.add_played()
        man.add_won()
        self.assertEqual(man.get_name(), 'test')
        self.assertEqual(man.get_coins(), 200)
        self.assertEqual(man.get_played(), 1)
        self.assertEqual(man.get_won(), 1)

    def test_eoo(self):
        game = EvenOrOdd(["Alice"])
        game.play()
        self.assertEqual(len(game.get_result()), len(["Alice"]))

    def test_minz(self):
        game = Minz(["Alice", "Bob", "Carol"])
        game.play()
        self.assertEqual(len(game.get_result()), len(["Alice", "Bob", "Carol"]))

    def test_bunco(self):
        game = Bunco(["Alice", "Bob", "Carol"])
        game.play()
        self.assertEqual(len(game.get_result()), len(["Alice", "Bob", "Carol"]))


if __name__ == "__main__":
    unittest.main()
