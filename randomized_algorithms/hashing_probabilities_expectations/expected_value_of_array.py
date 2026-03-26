from typing import List

class ExpectedValueCalculator:
    
    # Time Complexity: O(N)
    # Space Complexity: O(1)
    def calculate_expectation(self, arr: List[float]) -> float:
        n = len(arr)
        if n == 0:
            return 0.0
            
        # For a standard array, the probability of drawing any single element 
        # at random is uniformly 1 / n
        probability = 1.0 / n
        
        expected_value = 0.0
        
        # E[X] = sum(x_i * p_i)
        for num in arr:
            expected_value += num * probability
            
        return expected_value

# --- DRIVER CODE (EXAMPLE USAGE) ---
calculator = ExpectedValueCalculator()

# Example 1: Rolling a standard 6-sided die
dice_faces = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
print("Expected value of a fair 6-sided die (Expected: 3.5):", calculator.calculate_expectation(dice_faces))

# Example 2: Random array
arr = [1.0, 9.0, 6.0, 7.0, 8.0, 12.0]
print("Expected value of array [1, 9, 6, 7, 8, 12] (Expected: 7.166...):", calculator.calculate_expectation(arr))


'''
PROBABILISTIC ANALYSIS & PROOF (Expected Value / Mathematical Expectation)

A) Core Mathematical Definition:
   In probability theory, the Expected Value (or Expectation) of a discrete random 
   variable X, denoted as E[X], is the probability-weighted average of all its 
   possible values. 
   Formula: E[X] = Σ (x_i * P(x_i))
   where x_i is the value of the i-th outcome, and P(x_i) is the probability of 
   that outcome occurring.

B) Application to a Given Array:
   If we have an array of 'n' numbers and we pick one number completely at random 
   (uniform distribution), the probability P(x_i) of picking any specific element is 
   exactly 1/n.
   Substituting this into the expectation formula:
   E[X] = Σ (x_i * (1/n)) 
   E[X] = (1/n) * Σ x_i
   
   This mathematical proof demonstrates why the Expected Value of a uniform set of 
   numbers is algebraically identical to the standard Arithmetic Mean (Average).

C) Law of Large Numbers (LLN):
   Why is EV so important? The Law of Large Numbers states that if you perform the 
   same experiment (like picking a random element from the array) an infinite number 
   of times, the arithmetic mean of your actual empirical results will converge 
   almost surely to the theoretical Expected Value (E[X]). 
   For example, if you roll a 6-sided die millions of times, the sum of all rolls 
   divided by the number of rolls will perfectly approach 3.5.
'''