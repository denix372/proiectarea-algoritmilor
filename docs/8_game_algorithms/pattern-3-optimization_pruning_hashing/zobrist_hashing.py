import random
from typing import List

class ZobristHashing:
    def __init__(self):
        # Map chess pieces to integer indices (0 to 11)
        self.piece_map = {
            'P': 0, 'N': 1, 'B': 2, 'R': 3, 'Q': 4, 'K': 5,  # White pieces
            'p': 6, 'n': 7, 'b': 8, 'r': 9, 'q': 10, 'k': 11 # Black pieces
        }
        
        # Initialize a 3D table [8 rows][8 cols][12 piece types] with random 64-bit integers
        self.table = [[[random.getrandbits(64) for _ in range(12)] for _ in range(8)] for _ in range(8)]

    # Time Complexity: O(64) -> O(1) for an 8x8 board
    def compute_initial_hash(self, board: List[List[str]]) -> int:
        board_hash = 0
        for r in range(8):
            for c in range(8):
                piece = board[r][c]
                if piece != '-':
                    piece_idx = self.piece_map[piece]
                    # XOR the random number corresponding to this specific piece at this specific square
                    board_hash ^= self.table[r][c][piece_idx]
        return board_hash

    # Time Complexity: O(1)
    def update_hash(self, current_hash: int, r1: int, c1: int, r2: int, c2: int, piece: str) -> int:
        piece_idx = self.piece_map[piece]
        
        # 1. XOR out the piece from its old position
        current_hash ^= self.table[r1][c1][piece_idx]
        
        # 2. XOR in the piece at its new position
        current_hash ^= self.table[r2][c2][piece_idx]
        
        return current_hash

# --- DRIVER CODE (EXAMPLE USAGE) ---
zobrist = ZobristHashing()

# Initial 8x8 Chess Board Configuration
board = [
    list("---K----"),
    list("-R----Q-"),
    list("--------"),
    list("-P----p-"),
    list("-----p--"),
    list("--------"),
    list("p---b--q"),
    list("----n--k")
]

print("--- Zobrist Hashing Simulator ---")
# 1. Calculate full hash from scratch
initial_hash = zobrist.compute_initial_hash(board)
print(f"Initial Board Hash     : {initial_hash}")

# 2. Simulate moving the White King 'K' from (0,3) to (0,2)
piece = 'K'
r1, c1 = 0, 3
r2, c2 = 0, 2

# Apply the move in O(1)
new_hash = zobrist.update_hash(initial_hash, r1, c1, r2, c2, piece)
print(f"Hash after King moves  : {new_hash}")

# 3. Undo the move to verify the hash returns to its exact original state
# Moving it back from (0,2) to (0,3)
restored_hash = zobrist.update_hash(new_hash, r2, c2, r1, c1, piece)
print(f"Hash after undoing move: {restored_hash}")

assert initial_hash == restored_hash, "Hash properties violated!"
print()

'''
GAME THEORY ANALYSIS & PROOF (Zobrist Hashing & Transposition Tables)

A) Core Mathematical Idea (Properties of XOR):
   Zobrist hashing heavily relies on the bitwise XOR operator, which holds the 
   following mathematical properties:
   1. Commutativity: A ^ B = B ^ A
   2. Associativity: A ^ (B ^ C) = (A ^ B) ^ C
   3. Nilpotency: A ^ A = 0
   4. Identity: A ^ 0 = A

   Because of these properties, the order in which pieces are added to the hash 
   does not matter. More importantly, if a piece's random value 'V' is currently 
   XORed into the hash 'H', doing H ^ V effectively mathematically removes 'V' 
   from the hash without needing to recalculate the rest of the board.

B) Connection to The Birthday Paradox (Collisions):
   We are mapping an enormous state space (10^43 legal chess positions) into a 
   64-bit integer space (2^64 ≈ 1.8 * 10^19). 
   By the Birthday Paradox, collisions will eventually occur. However, within a 
   single search tree of a chess engine evaluating millions of nodes, the 
   probability of a collision using 64-bit numbers is astronomically low. 
   If a collision does occur, the engine might evaluate a board incorrectly, 
   but this risk is negligible compared to the massive speedup gained.

C) Transposition Tables:
   During Alpha-Beta / Iterative Deepening, whenever the AI computes a score for 
   a board state, it saves it in a Hash Map: `Memo[zobrist_hash] = Score`. 
   If the AI reaches the same physical board state via a different sequence of 
   moves (a transposition), it fetches the score in O(1) time instead of re-searching 
   the entire branch, exponentially reducing the search space.
'''