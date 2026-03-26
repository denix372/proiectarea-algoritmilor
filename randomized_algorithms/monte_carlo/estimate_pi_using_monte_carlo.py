import random

class MonteCarloPi:
    
    def estimate_pi(self, iterations: int) -> float:
        circle_points = 0
        
        for _ in range(iterations):
            x = random.random()
            y = random.random()
            
            if x * x + y * y <= 1.0:
                circle_points += 1
                
        # Calculate the estimation of Pi
        # pi / 4 = circle_points / iterations => pi = 4 * (circle_points / iterations)
        estimated_pi = 4 * (circle_points / iterations)
        
        return estimated_pi

simulator = MonteCarloPi()
print("--- Estimating Pi using Monte Carlo ---")
test_iterations = [10**3, 10**5, 10**7]

for n in test_iterations:
    pi_val = simulator.estimate_pi(n)
    print(f"Iterations: {n:<8} | Estimated Pi: {pi_val}")
print()

'''
PROBABILISTIC ANALYSIS & PROOF (Monte Carlo Estimation of Pi)

A) Core Mathematical Idea:
   Imagine a square of side length 2r centered at the origin (0,0). 
   Inside this square, we inscribe a circle of radius r.
   - Area of the Square = (2r) * (2r) = 4r^2
   - Area of the Circle = π * r^2
   
   The ratio of the areas is:
   Ratio = (Area of Circle) / (Area of Square) = (π * r^2) / (4r^2) = π / 4

B) The Monte Carlo Method:
   If we uniformly scatter random points across the square, the probability 'P' 
   that a point lands inside the inscribed circle is exactly equal to the ratio 
   of their geometric areas.
   P = (Points inside Circle) / (Total Points generated) = π / 4

C) Algorithm Logic:
   To simplify computation and avoid generating negative numbers, we only simulate 
   the first quadrant (x and y between 0 and 1). The area ratio remains exactly the same.
   - We generate random pairs (x, y) where 0 <= x < 1 and 0 <= y < 1.
   - A point lies inside the quarter-circle if its distance from the origin is <= 1.
   - Condition: x^2 + y^2 <= 1 (by the Pythagorean theorem).
   - We multiply the final probability by 4 to estimate the full value of Pi:
     π ≈ 4 * (circle_points / total_points)

D) Law of Large Numbers & Accuracy:
   Because this is a Monte Carlo simulation, the accuracy of the estimation depends 
   entirely on the number of iterations. The error decreases proportionally to 
   1 / sqrt(N). It is a probabilistic approximation, not a deterministic calculation.
   
E) Complexity:
   - Time Complexity: O(N), where N is the number of iterations.
   - Space Complexity: O(1) auxiliary space, as we only maintain counters.
'''