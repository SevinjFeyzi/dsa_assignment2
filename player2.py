# In this file you will find the player class for player 2.
# You may add additional smarts if you wish... but just using the game tree once it is properly created is fine

from a3_partb import GameTree

class PlayerTwo:

    def __init__(self, name = "P2 Bot",level = 4):
        self.name = name
        self.level = level

    def get_name(self):
        return self.name

    def get_play(self, board):
        tree = GameTree(board, -1 , tree_height = self.level)
        (row,col) = tree.get_move()
        return (row,col)