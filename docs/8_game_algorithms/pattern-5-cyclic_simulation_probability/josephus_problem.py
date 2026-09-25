class JosephusProblem:
    def find_survivor(self, n: int, k: int) -> int:
        # We use 0-based indexing for the math to work smoothly with the modulo operator.
        # Base case: if there is only 1 person (i=1), they are at index 0.
        survivor = 0
        
        # We build the solution from a circle of size 2 up to a circle of size n
        for circle_size in range(2, n + 1):
            # The survivor's position shifts by 'k' for each person added back to the circle
            survivor = (survivor + k) % circle_size
            
        # Convert back to 1-based indexing for the final answer
        return survivor + 1

n = 7
k = 3
print(JosephusProblem().find_survivor(n, k))
    

'''
MATHEMATICAL ANALYSIS & PROOF (Dynamic Programming / Recurrence)

A) Core Mathematical Idea (Shrinking the Circle):
   Imagine n people in a circle (0-indexed from 0 to n-1). 
   When the k-th person is executed, they are at index (k-1) % n.
   After this execution, the circle shrinks to n-1 people. The counting for the 
   next round starts exactly from the person who was sitting NEXT to the victim.
   
   If we know the safe position for (n-1) people, we can map that position back 
   to the original circle of n people simply by shifting it forward by 'k' 
   positions and wrapping around using modulo 'n'.

B) The Recurrence Relation:
   Let J(n, k) be the safe position for n people (0-indexed).
   J(1, k) = 0  (If there is only 1 person, they are safe at index 0)
   J(n, k) = (J(n-1, k) + k) % n
   
   Instead of using Recursion (which would take O(N) memory for the call stack 
   and risk a StackOverflow for large N), we compute this iteratively bottom-up, 
   starting from 2 people up to N.

C) Complexity:
   - Time Complexity: O(N). We execute a single loop from 2 to N, doing one 
     addition and one modulo operation per step.
   - Space Complexity: O(1). We only maintain a single integer variable ('survivor'), 
     making this the most memory-efficient approach possible.
'''