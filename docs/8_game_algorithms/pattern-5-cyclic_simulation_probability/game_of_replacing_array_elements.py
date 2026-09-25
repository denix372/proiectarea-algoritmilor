def play_game(arr: list[int]) -> int:
    unique_count = len(set(arr))
    
    # If the number of distinct elements is even, Player 1 wins
    # Otherwise, Player 2 wins
    return 1 if unique_count % 2 == 0 else 2

arr = [1, 1, 2, 2, 2, 2]
print(f"Player {play_game(arr)} Wins")

'''
GAME THEORY ANALYSIS & PROOF (Parity of Distinct Elements)

A) Core Mathematical Idea (State Reduction):
   In each move, a player picks two distinct numbers (e.g., a and b) and replaces 
   all occurrences of 'b' with 'a'. 
   Regardless of how many copies of 'a' and 'b' exist in the array, this operation 
   always strictly reduces the total count of distinct elements in the array by exactly 1.

B) Move Counting and Parity:
   Let U be the initial number of unique (distinct) elements in the array.
   The game ends when U reaches 1 (since 2 distinct elements are required to make a move).
   Therefore, the total number of valid moves in the entire game is exactly U - 1.
   
   - If U is EVEN: U - 1 is ODD. Player 1 makes the 1st, 3rd, ..., and the final (odd) move. Player 1 wins.
   - If U is ODD: U - 1 is EVEN. Player 2 makes the 2nd, 4th, ..., and the final (even) move. Player 2 wins.

C) Complexity:
   - Time Complexity: O(N) to convert the array to a hash set and count the unique elements.
   - Space Complexity: O(N) to store the unique elements in the set.
'''