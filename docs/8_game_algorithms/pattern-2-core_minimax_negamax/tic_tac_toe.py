class TicTacToeAI:
    def __init__(self):
        self.player = 'x'    # Maximizer (AI)
        self.opponent = 'o'  # Minimizer (Human)

    def is_moves_left(self, board: list[list[str]]) -> bool:
        for row in range(3):
            for col in range(3):
                if board[row][col] == '_':
                    return True
        return False

    def evaluate(self, board: list[list[str]]) -> int:
        # Check rows for victory
        for row in range(3):
            if board[row][0] == board[row][1] == board[row][2]:
                if board[row][0] == self.player:
                    return 10
                elif board[row][0] == self.opponent:
                    return -10

        # Check columns for victory
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col]:
                if board[0][col] == self.player:
                    return 10
                elif board[0][col] == self.opponent:
                    return -10

        # Check diagonals for victory
        if board[0][0] == board[1][1] == board[2][2]:
            if board[0][0] == self.player:
                return 10
            elif board[0][0] == self.opponent:
                return -10

        if board[0][2] == board[1][1] == board[2][0]:
            if board[0][2] == self.player:
                return 10
            elif board[0][2] == self.opponent:
                return -10

        # No winner yet
        return 0

    def minimax(self, board: list[list[str]], depth: int, is_max: bool) -> int:
        score = self.evaluate(board)

        # If Maximizer has won, deduct depth to favor faster wins
        if score == 10:
            return score - depth

        # If Minimizer has won, add depth to prolong the game
        if score == -10:
            return score + depth

        # If it's a tie
        if not self.is_moves_left(board):
            return 0

        if is_max:
            best = -1000
            for i in range(3):
                for j in range(3):
                    if board[i][j] == '_':
                        # Make the move
                        board[i][j] = self.player
                        # Call minimax recursively
                        best = max(best, self.minimax(board, depth + 1, not is_max))
                        # Undo the move
                        board[i][j] = '_'
            return best
        else:
            best = 1000
            for i in range(3):
                for j in range(3):
                    if board[i][j] == '_':
                        # Make the move
                        board[i][j] = self.opponent
                        # Call minimax recursively
                        best = min(best, self.minimax(board, depth + 1, not is_max))
                        # Undo the move
                        board[i][j] = '_'
            return best

    def find_best_move(self, board: list[list[str]]) -> tuple[int, int]:
        best_val = -1000
        best_move = (-1, -1)

        # Traverse all empty cells, evaluate minimax function for each
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    # Make the temporary move
                    board[i][j] = self.player
                    
                    # Compute evaluation function for this move.
                    # It's now the opponent's turn, so is_max is False
                    move_val = self.minimax(board, 0, False)
                    
                    # Undo the move
                    board[i][j] = '_'

                    # If the value of the current move is better than the best value, update
                    if move_val > best_val:
                        best_move = (i, j)
                        best_val = move_val

        return best_move

# Board State:
# x | o | x
# o | o | x
# _ | _ | _
board = [
    ['x', 'o', 'x'],
    ['o', 'o', 'x'],
    ['_', '_', '_']
]

print("--- Tic-Tac-Toe AI (Minimax) ---")
best_move = TicTacToeAI().find_best_move(board)
print(f"The Optimal Move is: ROW {best_move[0]} COL {best_move[1]}")
print()

'''
GAME THEORY ANALYSIS & PROOF (Minimax Algorithm)

A) Core Mathematical Idea (Zero-Sum Games):
   Tic-Tac-Toe is a finite, perfect-information, zero-sum game. 
   "Zero-sum" means one player's advantage is exactly the other player's loss.
   The algorithm models this by having Player A (Maximizer) aim for +10, 
   and Player B (Minimizer) aim for -10.

B) Backward Induction:
   The algorithm generates the entire game tree down to the terminal states 
   (win, lose, tie). It then propagates the scores back up to the root.
   At each level, the algorithm assumes the opponent plays optimally. 
   If a move leads to a branch where the opponent can force a loss (-10), 
   the Maximizer will absolutely avoid that branch.

C) Depth Penalty (The Tie-Breaker):
   Without depth penalty, an AI might choose a path that wins in 5 moves over 
   a path that wins in 1 move, because both paths return +10.
   By subtracting 'depth' from the winning score (10 - depth), immediate wins 
   become mathematically strictly greater than delayed wins (e.g., 9 > 5).
   Conversely, (-10 + depth) ensures the AI delays a forced loss as long as possible.

D) Complexity:
   - Time Complexity: O(b^d), where 'b' is the branching factor (available moves) 
     and 'd' is the depth of the tree. For Tic-Tac-Toe, it evaluates roughly 9! 
     (362,880) states in the worst case, making it O(1) conceptually for a fixed 3x3 board.
   - Space Complexity: O(d) for the recursive call stack depth, max 9.
'''