import unittest
from unittest.mock import patch
from logic import TicTacToe, Bot

class TestTicTacToe(unittest.TestCase):

    def setUp(self):
        self.game = TicTacToe()

    def test_empty_board_initialization(self):
        expected_board = [[None, None, None], [None, None, None], [None, None, None]]
        self.assertEqual(self.game.get_empty_board(), expected_board, "The board should be initialized with all None")

    def test_switch_player(self):
        initial_player = self.game.current_player
        self.game.switch_player()
        self.assertNotEqual(self.game.current_player, initial_player, "Switch player should change the current player")

    def test_check_winner_no_winner(self):
        self.assertIsNone(self.game.check_winner(), "There should be no winner for an empty board")

    def test_check_winner_row(self):
        self.game.board = [['X', 'X', 'X'], [None, None, None], [None, None, None]]
        self.assertEqual(self.game.check_winner(), 'X', "Player X should win with a complete row")

    def test_check_winner_column(self):
        self.game.board = [['O', None, None], ['O', None, None], ['O', None, None]]
        self.assertEqual(self.game.check_winner(), 'O', "Player O should win with a complete column")

    def test_check_winner_diagonal(self):
        self.game.board = [['X', None, None], [None, 'X', None], [None, None, 'X']]
        self.assertEqual(self.game.check_winner(), 'X', "Player X should win with a diagonal")

    def test_check_winner_draw(self):
        self.game.board = [['X', 'O', 'X'], ['X', 'X', 'O'], ['O', 'X', 'O']]
        self.assertEqual(self.game.check_winner(), 'draw', "The game should be a draw with no empty spaces and no winner")

class TestBot(unittest.TestCase):

    def setUp(self):
        self.bot = Bot()
        self.board = [[None, None, None], [None, None, None], [None, None, None]]

    def test_make_move(self):
        row, col = self.bot.make_move(self.board)
        self.assertIsNone(self.board[row][col], "Bot should select an empty position")

if __name__ == '__main__':
    unittest.main()
