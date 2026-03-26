import math

class BirthdayParadox:
    
    # 1. Exact calculation using probability multiplication
    # Time Complexity: O(N) where N is the returned number of people
    def find_min_people_exact(self, target_probability: float) -> int:
        if target_probability >= 1.0:
            return 367  # Pigeonhole Principle (365 days + leap year + 1)
            
        target_diff_prob = 1.0 - target_probability
        current_diff_prob = 1.0
        people = 1
        available_days = 365
        
        # We multiply the probability of the NEXT person having a unique birthday
        while current_diff_prob > target_diff_prob:
            available_days -= 1
            current_diff_prob *= (available_days / 365.0)
            people += 1
            
        return people

    # 2. Mathematical approximation using Taylor's Series
    # Time Complexity: O(1)
    def find_min_people_approx(self, target_probability: float) -> int:
        if target_probability >= 1.0:
            return 367
            
        # Formula derived from Taylor Series: n ≈ sqrt(2 * 365 * ln(1 / (1 - p)))
        exact_value = math.sqrt(2 * 365 * math.log(1 / (1 - target_probability)))
        return math.ceil(exact_value)


# --- DRIVER CODE (EXAMPLE USAGE) ---
simulator = BirthdayParadox()

targets = [0.50, 0.70, 0.999]
print("--- Birthday Paradox Estimates ---")
for p in targets:
    exact = simulator.find_min_people_exact(p)
    approx = simulator.find_min_people_approx(p)
    print(f"Target Probability: {p*100}% | Exact: {exact} people | Approx Formula: {approx} people")
print()

'''
PROBABILISTIC ANALYSIS & PROOF (Birthday Paradox & Polynomial Hashing)

A) Core Mathematical Idea:
   To find the probability that AT LEAST two people share a birthday, it is much easier 
   to calculate the complementary probability: that ALL people have DIFFERENT birthdays.
   P(Same) = 1 - P(Different)
   P(Different) = 1 * (364/365) * (363/365) * ... * (1 - (n-1)/365)

B) Taylor Series Approximation:
   Using the first-order Taylor expansion for e^x ≈ 1 + x (for very small x), 
   we can replace (1 - a/365) with e^(-a/365).
   The product becomes: e^(-1/365) * e^(-2/365) * ... * e^(-(n-1)/365)
   Adding the exponents (Sum of first n-1 integers is n(n-1)/2):
   P(Different) ≈ e^(-n(n-1) / 730) ≈ e^(-n^2 / 730)
   
   Solving P(Same) = 1 - e^(-n^2 / 730) for 'n' gives the inverse formula:
   n ≈ sqrt(2 * 365 * ln(1 / (1 - P(Same))))

C) Connection to Computer Science (Polynomial Hashing & Birthday Attack):
   The Birthday Paradox mathematically proves that if you randomly draw items from a 
   pool of size 'M', a collision is highly likely after drawing just sqrt(M) items.
   
   - Polynomial Hashing (Monte Carlo / Las Vegas):
     When converting strings to integers (Hashes) using H(s) = Σ s_i * B^i (mod M), 
     the hash space is M.
     If M = 2^32 (approx. 4.2 billion), you don't need 4 billion strings to get a collision. 
     By the Birthday Paradox, you will almost certainly get a hash collision after 
     processing only sqrt(2^32) = 2^16 = 65,536 strings!
     
   - Cryptography (Birthday Attack):
     This is why standard hash modulo M = 2^32 is easily broken. To ensure cryptographic 
     safety or a collision-free hash map (Monte Carlo logic becoming Las Vegas logic by 
     adding strict equality checks), we must use M = 10^18 (like the Mersenne prime 2^61 - 1) 
     or implement Double Hashing. For M = 10^18, a collision happens at roughly 
     sqrt(10^18) = 10^9 strings, which is computationally safe.

D) Complexity:
   - Exact Simulation: O(N) Time, O(1) Space.
   - Approximate Formula: O(1) Time, O(1) Space.
'''