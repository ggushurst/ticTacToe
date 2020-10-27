class TicTacToeBoard:
    def __init__(self):
        self.board = ['-','-','-',
                      '-','-','-',
                      '-','-','-']

    def getBoard(self):
        return self.board

    def showBoard(self):
        print('\n'.join(''.join(self.board[i:i+3]) for i in range(0,8,3)))

    def placeMove(self, player, position):
        if position.lower() == 'top left':
            if self.board[0] == '-':
                self.board[0] = player.upper()
                return True
            else:
                return False
        elif position.lower() == 'top middle':
            if self.board[1] == '-':
                self.board[1] = player.upper()
                return True
            else:
                return False        
        elif position.lower() == 'top right':
            if self.board[2] == '-':
                self.board[2] = player.upper()
                return True
            else:
                return False
        elif position.lower() == 'center left':
            if self.board[3] == '-':
                self.board[3] = player.upper()
                return True
            else:
                return False
        elif position.lower() == 'center':
            if self.board[4] == '-':
                self.board[4] = player.upper()
                return True
            else:
                return False
        elif position.lower() == 'center right':
            if self.board[5] == '-':
                self.board[5] = player.upper()
                return True
            else:
                return False
        elif position.lower() == 'bottom left':
            if self.board[6] == '-':
                self.board[6] = player.upper()
                return True
            else:
                return False
        elif position.lower() == 'bottom middle':
            if self.board[7] == '-':
                self.board[7] = player.upper()
                return True
            else:
                return False
        elif position.lower() == 'bottom right':
            if self.board[8] == '-':
                self.board[8] = player.upper()
                return True
            else:
                return False
        else:
            print("error on move placement")
            return False

    def checkWin(self, moveCount):
        if moveCount >= 4:
            for i in range(2):
                if self.board[i] == self.board[i+3] == self.board[i+6]:
                    return True
                else:
                    continue
            for j in [0, 3, 6]:
                if self.board[j] == self.board[j+1] == self.board[j+2]:
                    return True
                else:
                    continue
            if self.board[0] == self.board[4] == self.board[8]:
                return True
            elif self.board[6] == self.board[4] == self.board[2]:
                return True
            else:
                return False
        else:
            return False