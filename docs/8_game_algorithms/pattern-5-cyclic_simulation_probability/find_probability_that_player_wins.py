
def find_probability(p: int, q: int, r: int, s: int) -> float:
    prob_a = p / q
    prob_b = r / s
    t = (1 - prob_a) * (1 - prob_b)
    return round(prob_a / (1 - t), 9)

p, q, r, s = 1, 2, 1, 2
print(find_probability(p, q, r, s))

'''
GAME THEORY ANALYSIS & PROOF (Infinite Geometric Progression)

A) Mathematical Modeling:
   Let P(A) = p/q be the probability that Player 1 hits.
   Let P(B) = r/s be the probability that Player 2 hits.
   
   Player 1 wins if:
   - They hit on turn 1: P(A)
   - Both miss, then Player 1 hits on turn 3: (1 - P(A)) * (1 - P(B)) * P(A)
   - Both miss twice, then Player 1 hits: [(1 - P(A)) * (1 - P(B))]^2 * P(A)
   ... and so on indefinitely.

B) Geometric Series:
   This forms an infinite geometric progression:
   S = a + a*t + a*t^2 + ...
   
   Where:
   - First term 'a' = P(A)
   - Common ratio 't' = (1 - P(A)) * (1 - P(B))
   
   Since both probabilities are valid (t < 1), the sum of this infinite series 
   strictly converges to the formula: S = a / (1 - t).

C) Complexity:
   - Time Complexity: O(1). The infinite simulation is reduced to a single math formula.
   - Space Complexity: O(1).
'''