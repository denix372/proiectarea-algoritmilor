import random

class BiasedRandomGenerator:
    
    # Simulates a fair coin toss: returns 0 or 1 with 50% probability
    def rand50(self) -> int:
        # random.choice is used here strictly to simulate the API provided by the problem
        return random.choice([0, 1])

    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def rand75(self) -> int:
        # Generate two independent 50/50 bits
        bit1 = self.rand50()
        bit2 = self.rand50()
        
        # Bitwise OR operation
        return bit1 | bit2

# --- DRIVER CODE (EXAMPLE USAGE & EMPIRICAL PROOF) ---
generator = BiasedRandomGenerator()

print("--- Testing rand75() Distribution ---")
iterations = 100000
count_0 = 0
count_1 = 0

for _ in range(iterations):
    result = generator.rand75()
    if result == 1:
        count_1 += 1
    else:
        count_0 += 1

print(f"Total Iterations: {iterations}")
print(f"Number of 1s: {count_1} (Empirical Probability: {(count_1 / iterations) * 100:.2f}%) - Expected: 75.00%")
print(f"Number of 0s: {count_0} (Empirical Probability: {(count_0 / iterations) * 100:.2f}%) - Expected: 25.00%")
print()

'''
PROBABILISTIC ANALYSIS & ALGORITHM PROOF

A) Core Mathematical Idea:
   We are given a function rand50() that returns a Bernoulli random variable 
   where P(X = 0) = 0.5 and P(X = 1) = 0.5.
   We need to construct a new random variable Y such that P(Y = 1) = 0.75 and P(Y = 0) = 0.25.

B) Independence and Sample Space:
   By calling rand50() twice independently, we generate two variables, A and B.
   The sample space of the pair (A, B) has 4 equally likely outcomes:
   1. (0, 0) -> Probability: 0.5 * 0.5 = 0.25
   2. (0, 1) -> Probability: 0.5 * 0.5 = 0.25
   3. (1, 0) -> Probability: 0.5 * 0.5 = 0.25
   4. (1, 1) -> Probability: 0.5 * 0.5 = 0.25

C) Bitwise OR Logic:
   The Bitwise OR operator (|) evaluates to 0 if and only if BOTH operands are 0.
   Therefore, Y = A | B yields:
   - Y = 0 only for the outcome (0, 0).
     P(Y = 0) = 0.25 (25%)
     
   - Y = 1 for the outcomes (0, 1), (1, 0), and (1, 1).
     P(Y = 1) = 0.25 + 0.25 + 0.25 = 0.75 (75%)

D) Alternative Approaches:
   - Bitwise AND with Inversion: Y = (A & B) ^ 1. 
     A & B is 1 only 25% of the time (1,1). Inverting it gives 1 exactly 75% of the time.
   - Bit Shifting: Y = (A << 1) ^ B generates numbers 0, 1, 2, 3 with equal 25% probability. 
     Returning (Y > 0) maps {1,2,3} to 1 (75%) and {0} to 0 (25%).
   However, the Bitwise OR approach is computationally the most direct and elegant.
'''