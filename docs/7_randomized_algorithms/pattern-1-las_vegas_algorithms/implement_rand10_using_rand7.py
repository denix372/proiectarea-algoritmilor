import random
def rand7():
    return random.randint(1, 7)

# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            x = rand7()
            y = rand7()
            i = (x - 1) * 7 + y

            if i <= 40:
                return (i - 1) % 10 + 1
                
class Solution2:
    def rand10(self):
        while True:
            # First roll: generates 1 to 49
            a = rand7()
            b = rand7()
            idx = (a - 1) * 7 + b
            
            if idx <= 40:
                return (idx - 1) % 10 + 1
                
            # If idx is 41-49, we have 9 numbers. 
            # Recycle them! Get a new a (1 to 9) and roll a new b
            a = idx - 40
            b = rand7()
            
            # This generates a number from 1 to 63
            idx = (a - 1) * 7 + b
            
            if idx <= 60:
                return (idx - 1) % 10 + 1
                
            # If idx is 61-63, we have 3 numbers.
            # Recycle them! Get a new a (1 to 3) and roll a new b
            a = idx - 60
            b = rand7()
            
            # This generates a number from 1 to 21
            idx = (a - 1) * 7 + b
            
            if idx <= 20:
                return (idx - 1) % 10 + 1
                
            # If idx is 21, the loop restarts.

n = 3
res1 = []
res2 = []
for _ in range(n):
    res1.append(Solution().rand10())
    res2.append(Solution().rand10())
print(*res1)
print(*res2)

'''
INTERVIEW FOLLOW-UP ANSWERS:

Q1: What is the expected value for the number of calls to rand7() function?
Answer: 2.45 calls.

Mathematical Proof:
The standard approach uses 2 calls to rand7() to generate a number from 1 to 49.
The probability of "success" (getting a number from 1 to 40) is p = 40 / 49.
In statistics, the expected number of trials to get the first success in a 
Geometric Distribution is exactly 1 / p.
Expected trials = 1 / (40 / 49) = 49 / 40 = 1.225.
Since each trial requires exactly 2 calls to rand7():
Expected calls = 2 * 1.225 = 2.45.

---------------------------------------------------------

Q2: Could you minimize the number of calls to rand7()?
Answer: Yes, by recycling the rejected numbers, we can drop the expected calls to ~2.21.

Mathematical Proof (The Extreme Optimization):
Let E be the expected number of calls to rand7() to return a valid rand10().
1. We ALWAYS start with 2 calls. (Probability: 1)
   - If we land in 1-40 (Prob: 40/49), we are done.
   - If we land in 41-49 (Prob: 9/49), we reject and need 1 more call.
2. We make 1 additional call to pair with the 9 leftovers (9 * 7 = 63 space).
   - If we land in 1-60 (Prob: 60/63), we are done.
   - If we land in 61-63 (Prob: 3/63), we reject and need 1 more call.
3. We make 1 additional call to pair with the 3 leftovers (3 * 7 = 21 space).
   - If we land in 1-20 (Prob: 20/21), we are done.
   - If we land on 21 (Prob: 1/21), we reject and MUST RESTART the entire process (adding E calls).

We can express this as a recursive mathematical expectation:
E = 2(initial calls) + 
    (9/49) * 1(extra call) + 
    (9/49) * (3/63) * 1(extra call) + 
    (9/49) * (3/63) * (1/21) * E(restart cost)

Simplifying the fractions:
E = 2 + 9/49 + 1/49 + (1/343) * E
E = 2 + 10/49 + E / 343
E - E/343 = 108/49
(342/343) * E = 756/343

Multiply both sides by 343:
342 * E = 756
E = 756 / 342 ≈ 2.2105...

By recycling, we mathematically proved the expected calls decrease from 2.45 to 2.21.
'''