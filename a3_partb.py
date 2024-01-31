from a3_parta import evaluate_board
from a1_partd import overflow
from a1_partc import Queue


def copy_board(board):
        current_board = []
        height = len(board)
        for i in range(height):
            current_board.append(board[i].copy())
        return current_board

class GameTree:
    class Node:
        def __init__(self, board, depth, player, tree_height=4, move=None):
            """
            Initialize a node in the game tree.

            Parameters:
                - board (list): A 2D grid representing the game board.
                - depth (int): The depth of the node in the tree.
                - player (int): The player associated with the node.
                - tree_height (int): The maximum height of the game tree.
                - move (tuple): The move that led to this node.
            """
            self.board = copy_board(board)
            self.depth = depth
            self.player = player
            self.children = []
            self.move = move
            self.tree_height = tree_height

    def __init__(self, board, player, tree_height=4):
        """
        Initialize the GameTree with the initial game board.

        Parameters:
            - board (list): A 2D grid representing the initial game board.
            - player (int): The player who is making the move.
            - tree_height (int): The maximum height of the game tree.
        """
        self.player = player
        self.board = copy_board(board)
        self.root = self.Node(board, 0, player, tree_height)
        self.tree_height = tree_height

    def get_player(self, value):
        """
        Get the player associated with a specific value.

        Parameters:
            - value (int): The value representing a player or an empty cell.

        Returns:
            - int: The player associated with the value.
        """
        return 0 if value == 0 else value // abs(value)

    def clear_tree(self):
        """Clear all nodes in the game tree."""
        self.root.children = []

    def get_move(self):
        """
        Find and return the best move for the current player.

        Returns:
            - tuple: The coordinates (row, column) of the best move.
        """
        global BEST_MOVE
        height, width = len(self.board), len(self.board[0])
        BEST_MOVE = (0, 0) if self.player == 1 else (height - 1, width - 1)
        maxx = float('-inf')
        steps = float('inf')
        minn = float('inf')

        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.get_player(self.board[i][j]) == 0 or self.get_player(self.board[i][j]) == self.player:
                    
                    cp = copy_board(self.board)
                    cp[i][j] += self.player
                    q = Queue()
                    osteps = overflow(cp, q)
                    new_board = None

                    if osteps == 0:
                        new_board = cp

                    while not q.is_empty():
                        new_board = q.dequeue()

                    score =  evaluate_board(new_board, self.player)
                    if score >= maxx:
                        maxx = score
                        BEST_MOVE = (i, j)

                    tmp = self.minimax(self.board, 2, -1*self.player, (i, j))
                    if tmp[0] == float('inf'):
                        continue

                    if tmp[0] < minn and tmp[1] <= steps:
                        minn = tmp[0]
                        steps = tmp[1]
                        BEST_MOVE = (i, j)

        return BEST_MOVE

    def minimax(self, board, depth, player, move):
        """
        Perform the minimax algorithm to evaluate the best move.

        Parameters:
            - board (list): The game board.
            - depth (int): The current depth in the game tree.
            - player (int): The player making the move.
            - move (tuple): The move that led to this node.

        Returns:
            - list: A list containing the score and depth of the best move.
        """
        if depth >= self.tree_height:
            score =  evaluate_board(board, player)
            return [score,depth]

        score =  evaluate_board(board, player)
        if score == float('inf') or score == float('-inf'):
            return [score,depth]

        maxx = float('-inf')
        # minn = float('inf')
        for i in range(len(board)):
            for j in range(len(board[i])):
                if self.get_player(board[i][j]) == 0 or self.get_player(board[i][j]) == player:                        
                    cp = copy_board(board)
                    cp[i][j] += player

                    queue = Queue()
                    of_steps = overflow(cp, queue)
                    new_board = None

                    if of_steps == 0:
                        new_board = cp

                    while not queue.is_empty():
                        new_board = queue.dequeue()

                    score =  evaluate_board(new_board, player)

                    if score == float('-inf'):
                        continue

                    if score == float('inf'):
                        return [score,depth]

                    tmp = self.minimax(new_board, depth + 1, -1 * player, move)

                    if tmp[0] > maxx:
                        maxx = tmp[0]

        return [maxx,depth]
