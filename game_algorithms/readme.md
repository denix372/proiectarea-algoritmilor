# ♟️ Game Algorithms & Minimax Roadmap

**University Lab Primer:**
In zero-sum games (like Chess, Backgammon, or Tic-Tac-Toe), one player's gain is exactly the other player's loss. We traverse the game state using **Minimax**, but because writing separate `mini()` and `maxi()` functions duplicates code, we use **Negamax**: `score = -negamax(..., -beta, -alpha)`. 
To handle massive state spaces (like Chess), we use **Alpha-Beta Pruning** to cut off branches that are worse than previously found optimal moves, and **Iterative Deepening** to progressively search deeper while approximating unexplored states with a **Heuristic Evaluation Function**.

---

## SECTION: Combinatorial Game Theory (CGT)
*Concept: Games of perfect information. The core of CGT revolves around reducing complex games to the "Game of Nim" using Nimbers (Grundy Numbers) and the Sprague-Grundy Theorem.*

### PATTERN: The Game of Nim & Grundy Numbers
#### Standard (Core Mechanics)
* Nim Game — LeetCode 292 https://leetcode.com/problems/nim-game/
* Find the winner in nim-game — GFG
* Combinatorial Game Theory (Sets 1-4: Nim, Grundy, Mex, Sprague-Grundy) — GFG
#### Practice (Pile Manipulations)
* Stone Game IX — LeetCode 2029 https://leetcode.com/problems/stone-game-ix/
* Find the winner of the game with N piles of boxes — GFG
* Predict the winner of the game | Sprague-Grundy — GFG
#### Niche (Math & Optimization)
* Game of Chocolates | Wythoff’s Game — GFG
* Number of ways for playing first move optimally in a NIM game — GFG
* Predict the winner of a card game removing K cards (Bitwise AND condition) — GFG

---

## SECTION: Minimax Algorithm & AI
*Concept: Algorithms for simulating state-space trees in two-player zero-sum games to find the optimal move.*

### PATTERN: Core Minimax & Negamax
#### Standard
* Flip Game II — LeetCode 294 https://leetcode.com/problems/flip-game-ii/
* Implementation of Tic-Tac-Toe game (Minimax Sets 1-3) — GFG
#### Practice
* Predict the Winner — LeetCode 486 https://leetcode.com/problems/predict-the-winner/
* Guess the Word (Minimax heuristic elimination) — LeetCode 843 https://leetcode.com/problems/guess-the-word/
#### Niche
* Chessboard Pawn-Pawn game — GFG
* Ultimate Tic-Tac-Toe (Advanced state-space from RO Lab)

### PATTERN: Optimization (Pruning & Hashing)
#### Standard
* Minimax Algorithm in Game Theory | Set 4 (Alpha-Beta Pruning) — GFG
* Iterative Deepening & Heuristic Evaluation (From RO Lab: Chess/Backgammon/Go)
#### Practice
* Minimax Algorithm in Game Theory | Set 5 (Zobrist Hashing) — GFG
#### Niche
* Choice of Area (Game Theory state evaluation) — GFG

---

## SECTION: Ad-Hoc Game Logic & Game DP Simulation
*Concept: Games solved via localized math properties, combinatorial simulation, or specialized game dynamic programming (excluding standard interval DP).*

### PATTERN: Stone Games & Array Reductions
#### Standard
* Stone Game — LeetCode 877 https://leetcode.com/problems/stone-game/
* Stone Game II — LeetCode 1140 https://leetcode.com/problems/stone-game-ii/
#### Practice
* Stone Game III — LeetCode 1406 https://leetcode.com/problems/stone-game-iii/
* Stone Game IV — LeetCode 1510 https://leetcode.com/problems/stone-game-iv/
* Find winner in game of N balls (Range A, B removal) — GFG
#### Niche
* Stone Game VI — LeetCode 1686 https://leetcode.com/problems/stone-game-vi/
* Stone Game VIII — LeetCode 1872 https://leetcode.com/problems/stone-game-viii/
* Minimum operations to reduce N to a prime number by subtracting with its highest divisor — GFG

### PATTERN: Cyclic Simulation & Probability
#### Standard
* Josephus Problem — GFG
* Find probability that a player wins when probabilities of hitting the target are given — GFG
#### Practice
* Game of replacing array elements — GFG
* Find the player who wins the game by removing the last of given N cards — GFG
* Find the player who will win by choosing a number in range [1, K] with sum total N — GFG
#### Niche
* The prisoner’s dilemma in Game theory — GFG
* Find the winner of the Game to Win by erasing any two consecutive similar alphabets — GFG
* Winner in the Rock-Paper-Scissor game using Bit manipulation — GFG

Source: [GFG](https://www.geeksforgeeks.org/dsa/game-theory/)