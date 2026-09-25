# ♟️ Game Algorithms & Minimax Roadmap

**University Lab Primer:**
In zero-sum games (like Chess, Backgammon, or Tic-Tac-Toe), one player's gain is exactly the other player's loss. We traverse the game state using **Minimax**, but because writing separate `mini()` and `maxi()` functions duplicates code, we use **Negamax**: `score = -negamax(..., -beta, -alpha)`. 
To handle massive state spaces (like Chess), we use **Alpha-Beta Pruning** to cut off branches that are worse than previously found optimal moves, and **Iterative Deepening** to progressively search deeper while approximating unexplored states with a **Heuristic Evaluation Function**.

---

## PATTERN: The Game of Nim & Grundy Numbers

[[PATTERN_CARD_HERE]]

*Concept: Games of perfect information. The core of Combinatorial Game Theory (CGT) revolves around reducing complex games to the "Game of Nim" using Nimbers (Grundy Numbers) and the Sprague-Grundy Theorem.*

### 🔥 Standard (Core Mechanics)
- [x] [Nim Game - LeetCode 292](./the_game_of_nim_and_grundy_numbers/nim_game.py) — https://leetcode.com/problems/nim-game/
- [x] [Find the winner in nim-game - GFG](https://www.geeksforgeeks.org/dsa/find-winner-nim-game/)
- [x] [Combinatorial Game Theory (Sets 1-4: Nim, Grundy, Mex, Sprague-Grundy) - GFG](https://www.geeksforgeeks.org/combinatorial-game-theory-set-1-introduction/)

### 🧩 Practice (Pile Manipulations)
- [x] [Stone Game IX - LeetCode 2029](./stone_games_and_array_reductions/stone_game.py) — https://leetcode.com/problems/stone-game-ix/
- [x] [Find the winner of the game with N piles of boxes - GFG](./the_game_of_nim_and_grundy_numbers/find_the_winner_of_the_game_with_n_piles_of_boxes.py) — https://www.geeksforgeeks.org/dsa/find-the-winner-of-the-game-with-n-piles-of-boxes/
- [x] [Predict the winner of the game | Sprague-Grundy - GFG](./core_minimax_and_negamax/predict_the_winner.py) — https://www.geeksforgeeks.org/predict-the-winner-of-the-game-sprague-grundy/

### 🌀 Niche (Math & Optimization)
- [ ] [Game of Chocolates | Wythoff’s Game - GFG](https://www.geeksforgeeks.org/game-of-chocolates-wythoffs-game/)
- [] [Number of ways for playing first move optimally in a NIM game - GFG](./the_game_of_nim_and_grundy_numbers/nim_game.py) — https://www.geeksforgeeks.org/number-of-ways-for-playing-first-move-optimally-in-a-nim-game/
- [] [Predict the winner of a card game removing K cards (Bitwise AND condition) - GFG](./core_minimax_and_negamax/predict_the_winner.py) — https://www.geeksforgeeks.org/predict-the-winner-of-a-card-game-of-removing-k-cards-in-each-turn-such-that-bitwise-and-of-k-and-size-of-pile-is-0/

---

## PATTERN: Core Minimax & Negamax

[[PATTERN_CARD_HERE]]

*Concept: Algorithms for simulating state-space trees in two-player zero-sum games to find the optimal move.*

### 🔥 Standard
- [x] [Flip Game II - LeetCode 294](./core_minimax_and_negamax/flip_game_ii.py) — https://leetcode.ca/all/294.html
- [x] [Implementation of Tic-Tac-Toe game (Minimax Sets 1-3) - GFG](https://www.geeksforgeeks.org/implementation-of-tic-tac-toe-game/)

### 🧩 Practice
- [x] [Predict the Winner - LeetCode 486](./core_minimax_and_negamax/predict_the_winner.py) — https://leetcode.com/problems/predict-the-winner/
- [x] [Guess the Word (Minimax heuristic elimination) - LeetCode 843](./core_minimax_and_negamax/guess_the_word.py) — https://leetcode.com/problems/guess-the-word/

### 🌀 Niche
- [ ] [Chessboard Pawn-Pawn game - GFG](https://www.geeksforgeeks.org/chessboard-pawn-pawn-game/)
- [ ] [Ultimate Tic-Tac-Toe (Advanced state-space from RO Lab) - Wikipedia](https://en.wikipedia.org/wiki/Ultimate_tic-tac-toe)

---

## PATTERN: Optimization (Pruning & Hashing)

[[PATTERN_CARD_HERE]]

*Concept: Advanced techniques to reduce the search space and speed up Minimax algorithms.*

### 🔥 Standard
- [x] [Minimax Algorithm in Game Theory | Set 4 (Alpha-Beta Pruning) - GFG](https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-4-alpha-beta-pruning/)
- [x] [Iterative Deepening & Heuristic Evaluation (From RO Lab: Chess/Backgammon/Go) - Wikipedia](https://en.wikipedia.org/wiki/Iterative_deepening_depth-first_search)

### 🧩 Practice
- [x] [Minimax Algorithm in Game Theory | Set 5 (Zobrist Hashing) - GFG](./optimization_pruning_and_hashing/zobrist_hashing.py) — https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-5-zobrist-hashing/

### 🌀 Niche
- [ ] [Choice of Area (Game Theory state evaluation) - GFG](https://www.geeksforgeeks.org/dsa/game-theory-choice-area/)

---

## PATTERN: Stone Games & Array Reductions

[[PATTERN_CARD_HERE]]

*Concept: Ad-Hoc logic and games solved via localized math properties, combinatorial simulation, or specialized game dynamic programming (excluding standard interval DP).*

### 🔥 Standard
- [x] [Stone Game - LeetCode 877](./stone_games_and_array_reductions/stone_game.py) — https://leetcode.com/problems/stone-game/
- [x] [Stone Game II - LeetCode 1140](./stone_games_and_array_reductions/stone_game.py) — https://leetcode.com/problems/stone-game-ii/

### 🧩 Practice
- [x] [Stone Game III - LeetCode 1406](./stone_games_and_array_reductions/stone_game.py) — https://leetcode.com/problems/stone-game-iii/
- [x] [Stone Game IV - LeetCode 1510](./stone_games_and_array_reductions/stone_game.py) — https://leetcode.com/problems/stone-game-iv/
- [x] [Find winner in game of N balls (Range A, B removal) - GFG](./stone_games_and_array_reductions/find_winner_in_game_of_n_balls.py) — https://www.geeksforgeeks.org/find-winner-in-game-of-n-balls-in-which-a-player-can-remove-any-balls-in-range-a-b-in-a-single-move/

### 🌀 Niche
- [] [Stone Game VI - LeetCode 1686](./stone_games_and_array_reductions/stone_game.py) — https://leetcode.com/problems/stone-game-vi/
- [] [Stone Game VIII - LeetCode 1872](./stone_games_and_array_reductions/stone_game.py) — https://leetcode.com/problems/stone-game-viii/
- [ ] [Minimum operations to reduce N to a prime number by subtracting with its highest divisor - GFG](https://www.geeksforgeeks.org/dsa/minimum-operations-to-reduce-n-to-a-prime-number-by-subtracting-with-its-highest-divisor/)

---

## PATTERN: Cyclic Simulation & Probability

[[PATTERN_CARD_HERE]]

*Concept: Games solved via mathematical probability, string manipulation, or cyclic simulation.*

### 🔥 Standard
- [x] [Josephus Problem - GFG](./cyclic_simulation_and_probability/josephus_problem.py) — https://www.geeksforgeeks.org/josephus-problem/
- [x] [Find probability that a player wins when probabilities of hitting the target are given - GFG](https://www.geeksforgeeks.org/find-probability-that-a-player-wins-when-probabilities-of-hitting-the-target-are-given/)

### 🧩 Practice
- [x] [Game of replacing array elements - GFG](./cyclic_simulation_and_probability/game_of_replacing_array_elements.py) — https://www.geeksforgeeks.org/dsa/game-replacing-array-elements/
- [x] [Find the player who wins the game by removing the last of given N cards - GFG](https://www.geeksforgeeks.org/find-the-player-who-wins-the-game-by-removing-the-last-of-given-n-cards/)
- [x] [Find the player who will win by choosing a number in range [1, K] with sum total N - GFG](https://www.geeksforgeeks.org/find-the-player-who-will-win-by-choosing-a-number-in-range-1-k-with-sum-total-n/)

### 🌀 Niche
- [ ] [The prisoner’s dilemma in Game theory - GFG](https://www.geeksforgeeks.org/the-prisoners-dilemma-in-game-theory/)
- [ ] [Find the winner of the Game to Win by erasing any two consecutive similar alphabets - GFG](https://www.geeksforgeeks.org/find-the-winner-of-the-game-to-win-by-erasing-any-two-consecutive-similar-alphabets/)
- [ ] [Winner in the Rock-Paper-Scissor game using Bit manipulation - GFG](https://www.geeksforgeeks.org/winner-in-the-rock-paper-scissor-game-using-bit-manipulation/)

Source: [GFG Game Theory](https://www.geeksforgeeks.org/dsa/game-theory/)