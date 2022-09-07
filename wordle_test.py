from sys import stdin
import unittest

from wordle import Wordle


class WordleTest(unittest.TestCase):

    def test_parser_returns_letters_and_number(self):
        stdin = 'abcdefg'
        wordle = Wordle()
        simulated_user_input = wordle.get_inputs()
        self.assertEqual(simulated_user_input)





if __name__ == '__main__':
    unittest.main() 