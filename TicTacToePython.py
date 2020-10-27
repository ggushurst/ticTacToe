#TicTacToe Python
import TicTacToeBoard

board = TicTacToeBoard.TicTacToeBoard()
board.showBoard()
for x in range(9):
    board.showBoard()
    if x%2 == 0:

        player = "x"
    else:
        player = "y"

    validMove = False
    while not validMove:
        move = input("Please pick a space: ")
        validMove = board.placeMove(player, move)
    
    if board.checkWin(x):
        print("Congratulations player: " + player + " you have won the game!")
        break
    else:
        continue