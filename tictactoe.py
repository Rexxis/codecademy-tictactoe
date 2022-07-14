print("This is a Tic Tac Toe terminal game")
print("Created for Codecademy CS 101 Portfolio")
print("")
print("David Harendza - July 2022")

class TicTacToe:
    map = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
    def __init__(self):
        self.board = []

    def printboard(self):
        print(TicTacToe.map[:3])
        print(TicTacToe.map[4:6])
        print(TicTacToe.map[7:])

instance1 = TicTacToe()
instance1.printboard