import TicTacToeBoard
import unittest

class Test_TestTicTacToePython(unittest.TestCase):
    def test_showBoard(self):
        board = TicTacToeBoard.TicTacToeBoard()
        self.assertTrue(board.getboard())

    def test_placeMove(self):
        values = ['top left', 'top middle', 'top right', 'center left', 'center', 'center right', 'bottom left', 'bottom middle', 'bottom right']
        for value in values:
            print(value)
            self.failIfEqual(TicTacToeBoard.TicTacToeBoard.placeMove(self,'x',value), False)