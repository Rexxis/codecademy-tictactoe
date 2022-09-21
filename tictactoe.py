print("This is a Tic Tac Toe terminal game")
print("Created for Codecademy CS 101 Portfolio")
print("")
print("David Harendza - September 2022")
print("")

winner = None
gameRunning = None
currentPlayer = "X"

"""class Player:
    def __init__(self, player="X"):
        self.player = player
"""
class TicTacToe:

    def __init__(self):
        self.board = ["-","-","-","-","-","-","-","-","-"]

    def printboard(self):
        print("")
        print("BOARD POSITION")
        print(self.board[0], " | ", self.board[1], " | ", self.board[2])
        print("---------------")
        print(self.board[3], " | ", self.board[4], " | ", self.board[5])
        print("---------------")
        print(self.board[6], " | ", self.board[7], " | ", self.board[8])
        print("---------------")
    
    def playerInput(self):
        global currentPlayer
        print(f"Player {currentPlayer} turn")
        inp = int(input("Choose your position (1-9): "))
        if inp >= 1 and inp <= 9 and self.board[inp-1] == "-":
            self.board[inp-1] = currentPlayer
        else:
            print("Other player is already in the position. Choose other position!")

    def checkHorizontal(self):
        global winner
        if self.board[0] == self.board[1] == self.board[2] and self.board[1] != "-":
            winner = self.board[0]
            return True
        elif self.board[3] == self.board[4] == self.board[5] and self.board[3] != "-":
            winner = self.board[3]
            return True
        elif self.board[6] == self.board[7] == self.board[8] and self.board[6] != "-":
            winner = self.board[6]
            return True
    
    def checkRow(self):
        global winner
        if self.board[0] == self.board[3] == self.board[6] and self.board[0] != "-":
            winner = self.board[0]
            return True
        if self.board[1] == self.board[4] == self.board[7] and self.board[1] != "-":
            winner = self.board[1]
            return True
        if self.board[2] == self.board[5] == self.board[8] and self.board[2] != "-":
            winner = self.board[2]
            return True
    
    def checkDiag(self):
        global winner
        if self.board[0] == self.board[4] == self.board[8] and self.board[0] != "-":
            winner = self.board[0]
            return True
        if self.board[2] == self.board[4] == self.board[6] and self.board[2] != "-":
            winner = self.board[2]
            return True
    
    def checkTie(self):
        global gameRunning
        if "-" not in self.board:
            self.printboard()
            print("GAME OVER")
            print("It's a tie!")
            gameRunning = False

    def switchPlayer(self):
        global currentPlayer
        if currentPlayer == "X":
            currentPlayer = "O"
        else:
            currentPlayer = "X"
    
    def checkWin(self):
        global gameRunning
        if self.checkDiag() or self.checkHorizontal() or self.checkRow():
            self.printboard()
            print("GAME OVER")
            print(f"The winner is {winner}")
            gameRunning = False

instance1 = TicTacToe()

def refresh_screen():
    instance1.printboard()

def startGame():
    global gameRunning
    print("Select your desired position with this index:")
    print("BOARD POSITION")
    print("1", " | ", "2", " | ", "3")
    print("---------------")
    print("4", " | ", "5", " | ", "6")
    print("---------------")
    print("7", " | ", "8", " | ", "9")
    print("---------------")
    print("")
    if input("Are you ready to start the game ? (Y/N): ") == "Y":
        print("")
        print("GAME STARTED")
        gameRunning = True
    else:
        gameRunning = False

startGame()

while gameRunning:
    refresh_screen()
    instance1.playerInput()
    instance1.checkWin()
    if winner != None:
        break
    instance1.checkTie()
    instance1.switchPlayer()