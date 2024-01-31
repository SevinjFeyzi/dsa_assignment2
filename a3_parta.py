def evaluate_board(board, player):
    """
    Evaluate the current state of the game board for a given player.

    Parameters:
        - board (list): A 2D grid representing the game board.
        - player (int): The player for whom the board is being evaluated. +1 for Player 1, -1 for Player 2.

    Returns:
        - int: A score indicating the advantage of the board for the specified player.
               Positive values favor the player, negative values favor the opponent.

    The function considers the following conditions:
    - If the specified player wins, returns positive infinity.
    - If the opponent wins, returns negative infinity.
    - Calculates the difference in the number of pieces between the player and the opponent.

    Note: The board should follow specific conventions where:
    - 0 indicates an empty cell.
    - Positive numbers indicate Player 1's pieces.
    - Negative numbers indicate Player 2's pieces.
    """
    def check_winner(mover):
        """
        Check if the specified player (mover) has won the game.

        Parameters:
            - mover (int): The player for whom the win is being checked.

        Returns:
            - bool: True if the specified player has won, False otherwise.
        """
        for row in board:
            for cell in row:
                if cell == 0:
                    continue
                if int(abs(cell) / cell) != mover:
                    return False
        return True

    # Check if the specified player has won
    if check_winner(player):
        return float('inf')
    
    # Check if the opponent has won
    if check_winner(-player):
        return float('-inf')

    # Count the number of pieces for each player
    player1_pieces = sum(1 for row in board for cell in row if cell != 0 and int(abs(cell) / cell) == player)
    player2_pieces = sum(1 for row in board for cell in row if cell != 0 and int(abs(cell) / cell) == -player)

    # Return the score based on the difference in the number of pieces
    return player1_pieces - player2_pieces
