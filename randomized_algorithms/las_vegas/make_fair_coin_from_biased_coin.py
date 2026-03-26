
import random

def foo() -> int:
    if random.random() < 0.6:
        return 0
    else:
        return 1

class Solution:
    def make_fair_coin(self) -> int:
        while True:
            val1 = foo()
            val2 = foo()
            
            if val1 != val2:
                # Will reach here with 
                # (0.24 + 0.24) probability
                return val1

print(Solution().make_fair_coin())

'''
INTERVIEW EXPLANATION & MATHEMATICAL PROOF (John von Neumann's Trick)

A) Core Idea:
   We are given a biased coin where the probability of heads (1) is 'p' and 
   the probability of tails (0) is '1 - p'. 
   If we flip the coin twice, the outcomes are:
   - (0, 0) with probability (1 - p) * (1 - p)
   - (1, 1) with probability p * p
   - (0, 1) with probability (1 - p) * p
   - (1, 0) with probability p * (1 - p)
   
   Notice that the probability of getting (0, 1) is EXACTLY EQUAL to the 
   probability of getting (1, 0), regardless of how biased the coin is!
   Therefore, we flip the coin in pairs:
   - If the results match (0,0 or 1,1), we throw them away and flip again.
   - If we get (0,1), we output 0.
   - If we get (1,0), we output 1.
   This guarantees a perfectly 50/50 fair outcome.

B) Probabilistic Analysis & Expected Time Complexity:
   Let p = 0.4 (probability of 1) and (1 - p) = 0.6 (probability of 0).
   The probability of stopping (getting a valid pair) on any given iteration is:
   P(stop) = P(0,1) + P(1,0) 
           = (0.6 * 0.4) + (0.4 * 0.6) 
           = 0.24 + 0.24 = 0.48 (or 48%).

   This models a Geometric Distribution where the probability of "success" is q = 0.48.
   The expected number of paired flips to get a success is 1 / q.
   Expected paired flips = 1 / 0.48 ≈ 2.08.
   Since each pair requires 2 calls to foo(), the expected number of total foo() calls is:
   Expected calls = 2 * (1 / 0.48) = 4.16.

C) Complexity:
   - Time Complexity: Expected O(1) because the average number of calls is a constant (4.16). 
     However, the worst-case is theoretically O(infinity) if we keep getting (0,0) or (1,1) forever.
   - Space Complexity: O(1) auxiliary space (using a while loop avoids recursive call stack overhead).
'''