import random

class FreivaldsAlgorithm:
    
    # Helper method to multiply an N x N matrix with an N x 1 vector
    # Time Complexity: O(N^2)
    def _multiply_matrix_vector(self, mat: list[list[int]], vec: list[int], n: int) -> list[int]:
        result = [0] * n
        for i in range(n):
            for j in range(n):
                result[i] += mat[i][j] * vec[j]
        return result

    # Runs a single iteration of Freivald's test
    def _freivald_test(self, A: list[list[int]], B: list[list[int]], C: list[list[int]], n: int) -> bool:
        # 1. Generate a random N x 1 vector with elements strictly from {0, 1}
        r = [random.randint(0, 1) for _ in range(n)]
        
        # 2. Compute Br = B * r
        Br = self._multiply_matrix_vector(B, r, n)
        
        # 3. Compute Cr = C * r
        Cr = self._multiply_matrix_vector(C, r, n)
        
        # 4. Compute ABr = A * (B * r)
        ABr = self._multiply_matrix_vector(A, Br, n)
        
        # 5. Check if A*(B*r) == C*r
        for i in range(n):
            if ABr[i] != Cr[i]:
                return False  # Definitely not a product
                
        return True # Probably a product

    def is_product(self, A: list[list[int]], B: list[list[int]], C: list[list[int]], n: int, k: int = 5) -> bool:
        # Run the test k times to decrease the probability of a false positive
        for _ in range(k):
            if not self._freivald_test(A, B, C, n):
                return False
        return True


# --- DRIVER CODE (EXAMPLE USAGE) ---
freivald = FreivaldsAlgorithm()

# Example 1: Correct Product (A * B == C)
A1 = [[1, 1], 
      [1, 1]]
B1 = [[1, 1], 
      [1, 1]]
C1 = [[2, 2], 
      [2, 2]]
print("Is C1 the product of A1 and B1? (Expected True):", freivald.is_product(A1, B1, C1, 2))

# Example 2: Incorrect Product (A * B != C)
A2 = [[1, 1, 1], 
      [1, 1, 1], 
      [1, 1, 1]]
B2 = [[1, 1, 1], 
      [1, 1, 1], 
      [1, 1, 1]]
C2 = [[3, 3, 3], 
      [3, 1, 2], # Intentional error here
      [3, 3, 3]]
print("Is C2 the product of A2 and B2? (Expected False):", freivald.is_product(A2, B2, C2, 3))
print()

'''
PROBABILISTIC ANALYSIS & ALGORITHM PROOF (Freivald's Algorithm / Monte Carlo)

A) Core Mathematical Idea:
   Standard matrix multiplication of two N x N matrices A and B takes O(N^3) time 
   (or O(N^2.81) using Strassen's algorithm). 
   Freivald's algorithm avoids this by leveraging matrix associativity:
   A * (B * r) = (A * B) * r
   By generating a random N x 1 vector 'r', we transform matrix-matrix multiplications 
   into matrix-vector multiplications, which strictly take O(N^2) time.
   We then simply check if A * (B * r) == C * r.

B) Classification: Monte Carlo Algorithm
   - If A * B = C, the algorithm ALWAYS returns True (0% false negative rate).
   - If A * B != C, the algorithm might accidentally return True. This is a false positive.

C) Error Probability & Mathematical Proof:
   Let D = (A * B) - C. 
   If C is NOT the product, matrix D is non-zero (it has at least one non-zero element d_ij).
   When we multiply D by the random binary vector r (elements in {0, 1}), the resulting 
   vector is D * r.
   The probability that a specific row 'i' in D * r evaluates exactly to 0, despite d_ij != 0, 
   depends on the random coin flips of the vector 'r'.
   By the Principle of Deferred Decisions, the probability that the elements perfectly cancel 
   each other out is at most 1/2.
   Therefore, the probability of a false positive in a single run is P(error) <= 1/2.

D) Amplification (Law of Large Numbers):
   Since each iteration is completely independent, running the test 'k' times reduces 
   the error probability exponentially.
   After 'k' runs, P(error) <= (1/2)^k.
   For k = 10, the chance of a false positive is less than 0.1% (1 in 1024).

E) Complexity:
   - Time Complexity: O(k * N^2) 
     (3 matrix-vector multiplications per iteration, taking O(N^2) each).
   - Space Complexity: O(N) auxiliary space to store the random vector and intermediate result vectors.
'''