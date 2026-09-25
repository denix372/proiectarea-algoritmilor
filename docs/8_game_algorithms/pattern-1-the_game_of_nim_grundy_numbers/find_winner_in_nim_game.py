
def find_winner(nums):
    xor_sum = 0
    for num in nums:
        xor_sum ^= num
        
    # Alice wins if the initial XOR is already 0, 
    # OR if the array has an even number of elements.
    if xor_sum == 0 or len(nums) % 2 == 0:
        return "Alice"
    else:
        return "Bob"

arr = [1, 1]
print(findWinner(arr))

'''
GAME THEORY ANALYSIS & PROOF (XOR Nim-Game)

A) Core Mathematical Idea & Rules:
   - Players take turns removing one element.
   - If a player's removal causes the XOR sum of the remaining elements to become 0, 
     that player loses.
   - Let 'S' be the XOR sum of all elements currently in the array.
   - If S == 0 at the very beginning of the game, Alice wins by default (as per 
     specific problem rules, the game ends before she has to make a move).

B) Proof by Contradiction (Why EVEN length arrays always win):
   Suppose the array has an EVEN number of elements 'n' and S != 0.
   It is Alice's turn. Can she always find an element to remove such that the 
   new XOR sum is NOT 0?
   
   Let's assume the opposite (Contradiction Hypothesis): 
   Suppose NO MATTER WHAT element Alice chooses, the remaining XOR sum becomes 0.
   This means for every element A[i], removing it gives a XOR sum of 0:
   S ^ A[i] = 0  => This implies A[i] = S, for all i from 1 to n.
   
   If every element in the array is exactly equal to S, let's recalculate the 
   total XOR sum of the array:
   S = A[1] ^ A[2] ^ ... ^ A[n]
   S = S ^ S ^ ... ^ S (n times)
   
   Since 'n' is EVEN, the XOR sum of an even number of identical elements is always 0.
   So, S = 0.
   But wait! We started with the premise that S != 0. This is a CONTRADICTION!
   
   Conclusion: If 'n' is EVEN and S != 0, it is mathematically impossible for all 
   moves to result in 0. Therefore, Alice can ALWAYS find at least one safe move.

C) Game Flow (Odd vs Even):
   - If 'n' is EVEN (and S != 0): Alice makes a safe move. The array becomes ODD.
   - Now Bob faces an ODD array. Whatever he does, he leaves an EVEN array for Alice.
   - Because the person facing an EVEN array can always survive, the person facing 
     the ODD array is eventually forced to make a losing move (when only 1 element 
     is left, removing it leaves an empty array with XOR 0).
   - Thus, if initial 'n' is EVEN -> Alice wins. If initial 'n' is ODD -> Bob wins.
'''