# ♟️ Game Algorithms & Minimax Roadmap

**University Lab Primer:**
In zero-sum games (like Chess, Backgammon, or Tic-Tac-Toe), one player's gain is exactly the other player's loss. We traverse the game state using **Minimax**, but because writing separate `mini()` and `maxi()` functions duplicates code, we use **Negamax**: `score = -negamax(..., -beta, -alpha)`. 
To handle massive state spaces (like Chess), we use **Alpha-Beta Pruning** to cut off branches that are worse than previously found optimal moves, and **Iterative Deepening** to progressively search deeper while approximating unexplored states with a **Heuristic Evaluation Function**.

---

## PATTERN: The Game of Nim & Grundy Numbers
*Concept: Games of perfect information. The core of Combinatorial Game Theory (CGT) revolves around reducing complex games to the "Game of Nim" using Nimbers (Grundy Numbers) and the Sprague-Grundy Theorem.*

### 🔥 Standard (Core Mechanics)
* [Nim Game - LeetCode 292](https://leetcode.com/problems/nim-game/)
* [Find the winner in nim-game - GFG](https://www.geeksforgeeks.org/find-the-winner-in-nim-game/)
* [Combinatorial Game Theory (Sets 1-4: Nim, Grundy, Mex, Sprague-Grundy) - GFG](https://www.geeksforgeeks.org/combinatorial-game-theory-set-1-introduction/)

### 🧩 Practice (Pile Manipulations)
* [Stone Game IX - LeetCode 2029](https://leetcode.com/problems/stone-game-ix/)
* [Find the winner of the game with N piles of boxes - GFG](https://www.geeksforgeeks.org/dsa/find-the-winner-of-the-game-with-n-piles-of-boxes/)
* [Predict the winner of the game | Sprague-Grundy - GFG](https://www.geeksforgeeks.org/predict-the-winner-of-the-game-sprague-grundy/)

### 🌀 Niche (Math & Optimization)
* [Game of Chocolates | Wythoff’s Game - GFG](https://www.geeksforgeeks.org/game-of-chocolates-wythoffs-game/)
* [Number of ways for playing first move optimally in a NIM game - GFG](https://www.geeksforgeeks.org/number-of-ways-for-playing-first-move-optimally-in-a-nim-game/)
* [Predict the winner of a card game removing K cards (Bitwise AND condition) - GFG](https://www.geeksforgeeks.org/predict-the-winner-of-a-card-game-of-removing-k-cards-in-each-turn-such-that-bitwise-and-of-k-and-size-of-pile-is-0/)

---

## PATTERN: Core Minimax & Negamax
*Concept: Algorithms for simulating state-space trees in two-player zero-sum games to find the optimal move.*

### 🔥 Standard
* [Flip Game II - LeetCode 294](https://leetcode.com/problems/flip-game-ii/)
* [Implementation of Tic-Tac-Toe game (Minimax Sets 1-3) - GFG](https://www.geeksforgeeks.org/implementation-of-tic-tac-toe-game/)

### 🧩 Practice
* [Predict the Winner - LeetCode 486](https://leetcode.com/problems/predict-the-winner/)
* [Guess the Word (Minimax heuristic elimination) - LeetCode 843](https://leetcode.com/problems/guess-the-word/)

### 🌀 Niche
* [Chessboard Pawn-Pawn game - GFG](https://www.geeksforgeeks.org/chessboard-pawn-pawn-game/)
* [Ultimate Tic-Tac-Toe (Advanced state-space from RO Lab) - Wikipedia](https://en.wikipedia.org/wiki/Ultimate_tic-tac-toe)

---

## PATTERN: Optimization (Pruning & Hashing)
*Concept: Advanced techniques to reduce the search space and speed up Minimax algorithms.*

### 🔥 Standard
* [Minimax Algorithm in Game Theory | Set 4 (Alpha-Beta Pruning) - GFG](https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-4-alpha-beta-pruning/)
* [Iterative Deepening & Heuristic Evaluation (From RO Lab: Chess/Backgammon/Go) - Wikipedia](https://en.wikipedia.org/wiki/Iterative_deepening_depth-first_search)

### 🧩 Practice
* [Minimax Algorithm in Game Theory | Set 5 (Zobrist Hashing) - GFG](https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-5-zobrist-hashing/)

### 🌀 Niche
* [Choice of Area (Game Theory state evaluation) - GFG](https://www.geeksforgeeks.org/dsa/game-theory-choice-area/)

---

## PATTERN: Stone Games & Array Reductions
*Concept: Ad-Hoc logic and games solved via localized math properties, combinatorial simulation, or specialized game dynamic programming (excluding standard interval DP).*

### 🔥 Standard
* [Stone Game - LeetCode 877](https://leetcode.com/problems/stone-game/)
* [Stone Game II - LeetCode 1140](https://leetcode.com/problems/stone-game-ii/)

### 🧩 Practice
* [Stone Game III - LeetCode 1406](https://leetcode.com/problems/stone-game-iii/)
* [Stone Game IV - LeetCode 1510](https://leetcode.com/problems/stone-game-iv/)
* [Find winner in game of N balls (Range A, B removal) - GFG](https://www.geeksforgeeks.org/find-winner-in-game-of-n-balls-in-which-a-player-can-remove-any-balls-in-range-a-b-in-a-single-move/)

### 🌀 Niche
* [Stone Game VI - LeetCode 1686](https://leetcode.com/problems/stone-game-vi/)
* [Stone Game VIII - LeetCode 1872](https://leetcode.com/problems/stone-game-viii/)
* [Minimum operations to reduce N to a prime number by subtracting with its highest divisor - GFG](https://www.geeksforgeeks.org/dsa/minimum-operations-to-reduce-n-to-a-prime-number-by-subtracting-with-its-highest-divisor/)

---

## PATTERN: Cyclic Simulation & Probability
*Concept: Games solved via mathematical probability, string manipulation, or cyclic simulation.*

### 🔥 Standard
* [Josephus Problem - GFG](https://www.geeksforgeeks.org/josephus-problem/)
* [Find probability that a player wins when probabilities of hitting the target are given - GFG](https://www.geeksforgeeks.org/find-probability-that-a-player-wins-when-probabilities-of-hitting-the-target-are-given/)

### 🧩 Practice
* [Game of replacing array elements - GFG](https://www.geeksforgeeks.org/game-of-replacing-array-elements/)
* [Find the player who wins the game by removing the last of given N cards - GFG](https://www.geeksforgeeks.org/find-the-player-who-wins-the-game-by-removing-the-last-of-given-n-cards/)
* [Find the player who will win by choosing a number in range [1, K] with sum total N - GFG](https://www.geeksforgeeks.org/find-the-player-who-will-win-by-choosing-a-number-in-range-1-k-with-sum-total-n/)

### 🌀 Niche
* [The prisoner’s dilemma in Game theory - GFG](https://www.geeksforgeeks.org/the-prisoners-dilemma-in-game-theory/)
* [Find the winner of the Game to Win by erasing any two consecutive similar alphabets - GFG](https://www.geeksforgeeks.org/find-the-winner-of-the-game-to-win-by-erasing-any-two-consecutive-similar-alphabets/)
* [Winner in the Rock-Paper-Scissor game using Bit manipulation - GFG](https://www.geeksforgeeks.org/winner-in-the-rock-paper-scissor-game-using-bit-manipulation/)

Source: [GFG Game Theory](https://www.geeksforgeeks.org/dsa/game-theory/)