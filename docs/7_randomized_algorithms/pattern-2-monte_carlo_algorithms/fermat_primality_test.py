import random

class FermatPrimalityTest:
    
    # O(log exp) time complexity for modular exponentiation
    def modular_exponentiation(self, base: int, exp: int, mod: int) -> int:
        res = 1
        base = base % mod
        while exp > 0:
            if exp % 2 == 1:
                res = (res * base) % mod
            exp = exp // 2
            base = (base * base) % mod
        return res

    def is_prime(self, n: int, k: int = 5) -> bool:
        # Corner cases
        if n <= 1 or n == 4:
            return False
        if n <= 3:
            return True

        # Perform k independent tests
        for _ in range(k):
            # Pick a random base 'a' in the range [2, n - 2]
            a = random.randint(2, n - 2)
            
            # Fermat's Little Theorem condition: a^(n-1) ≡ 1 (mod n)
            if self.modular_exponentiation(a, n - 1, n) != 1:
                # If it doesn't equal 1, 'n' is DEFINITELY composite
                return False
                
        # If it passes k iterations, it is PROBABLY prime
        return True
    
fermat_test = FermatPrimalityTest()
print("--- Fermat Primality Test ---")
print("Is 97 prime? (Expected True):", fermat_test.isPrime(97))
print("Is 100 prime? (Expected False):", fermat_test.isPrime(100))
print("Is 561 prime? (Carmichael number - Fermat fails and returns True!):", fermat_test.isPrime(561))

'''
PROBABILISTIC ANALYSIS & PROOF (Fermat's Method)

A) Core Mathematical Theorem:
   Fermat's Little Theorem states that if 'p' is a prime number, then for any 
   integer 'a' such that 1 < a < p-1, the following congruence holds:
   a^(p-1) ≡ 1 (mod p)

B) Algorithm Logic (Probabilistic Test):
   - If we pick a random 'a' and a^(n-1) ≢ 1 (mod n), then 'n' is 100% composite. 
     The base 'a' is called a "Fermat witness".
   - If a^(n-1) ≡ 1 (mod n), 'n' might be prime. The base 'a' is a "Fermat liar".
   - By repeating the test 'k' times with random bases, we reduce the probability 
     of false positives.

C) The Fatal Flaw (Carmichael Numbers):
   Fermat's test is generally a great probabilistic algorithm, BUT it fails completely 
   for a specific subset of composite numbers known as Carmichael numbers (e.g., 561, 1105).
   A Carmichael number 'n' is composite, yet it satisfies a^(n-1) ≡ 1 (mod n) for 
   ALL bases 'a' that are coprime to 'n'. Thus, no matter how high 'k' is, Fermat's 
   test will consistently return "True" (Prime) for Carmichael numbers, making the 
   error rate unacceptably high for cryptographic systems.

D) Complexity:
   - Time Complexity: O(k * log n) where modular exponentiation takes O(log n) time.
   - Space Complexity: O(1) auxiliary space.
'''