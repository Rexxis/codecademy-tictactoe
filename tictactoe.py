print("This is a Tic Tac Toe terminal game")
print("Created for Codecademy CS 101 Portfolio")
print("")
print("David Harendza - September 2022")
print("")

winner = None

class Player:
    def __init__(self, player):
        self.player = player

class TicTacToe:

    def __init__(self):
        self.board = ["-","-","-","-","-","-","-","-","-"]

    def printboard(self):
        print("BOARD POSITION")
        print(self.board[0], " | ", self.board[1], " | ", self.board[2])
        print("---------------")
        print(self.board[3], " | ", self.board[4], " | ", self.board[5])
        print("---------------")
        print(self.board[6], " | ", self.board[7], " | ", self.board[8])
        print("---------------")
    
    def playerInput(self):
        inp0 = input("x or o player ? (enter x or o): ")
        if inp0 == "x":
            self.player = "x"
        elif inp0 == "o":
            self.player = "o"
        else:
            print("Please enter x or o!")

        inp = int(input("Choose your position (1-9): "))
        if inp >= 1 and inp <= 9 and self.board[inp-1] == "-":
            self.board[inp-1] = self.player
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


instance1 = TicTacToe()

def refresh_screen():
    instance1.printboard()

while True:
    refresh_screen()
    instance1.playerInput()
    refresh_screen()