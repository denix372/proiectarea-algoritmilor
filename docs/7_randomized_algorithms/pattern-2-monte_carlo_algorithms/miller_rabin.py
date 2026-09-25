import random

class MillerRabinPrimalityTest:
    
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
        if n <= 1 or n == 4:
            return False
        if n <= 3:
            return True

        # Write n - 1 as d * 2^s by factoring out powers of 2
        d = n - 1
        while d % 2 == 0:
            d //= 2

        # Perform k independent tests
        for _ in range(k):
            a = random.randint(2, n - 2)
            
            # Compute x = a^d % n
            x = self.modular_exponentiation(a, d, n)

            # If x is 1 or n - 1, the base passes the test (might be prime)
            if x == 1 or x == n - 1:
                continue

            # Keep squaring x while d does not reach n - 1
            # We are checking the sequence: a^d, a^(2d), a^(4d) ... a^((n-1)/2)
            temp_d = d
            while temp_d != n - 1:
                x = (x * x) % n
                temp_d *= 2

                # If x becomes 1, 'n' is composite (we found a non-trivial square root of 1)
                if x == 1:
                    return False
                # If x becomes n - 1, it passes this base's test
                if x == n - 1:
                    break
            else:
                # If the while loop finishes without hitting the 'break' (x == n - 1),
                # it means we never found -1 in the sequence. 'n' is composite.
                return False

        return True

miller_test = MillerRabinPrimalityTest()
print("--- Miller-Rabin Primality Test ---")
print("Is 97 prime? (Expected True):", miller_test.isPrime(97))
print("Is 100 prime? (Expected False):", miller_test.isPrime(100))
print("Is 561 prime? (Carmichael number - Miller-Rabin correctly returns False!):", miller_test.isPrime(561))

'''
PROBABILISTIC ANALYSIS & PROOF (Miller-Rabin / Monte Carlo)

A) Core Mathematical Idea (Fixing Fermat's Flaw):
   Miller-Rabin is built on top of Fermat's Little Theorem, but adds a crucial check 
   based on Euclid's Lemma: If n is prime, the only solutions to x^2 ≡ 1 (mod n) 
   are x ≡ 1 or x ≡ -1 (which is n-1). There are no "non-trivial" square roots of 1.

   Since 'n' is odd, 'n-1' is even, meaning we can write n-1 = d * 2^s.
   Instead of just checking a^(n-1) ≡ 1 (mod n), we compute a^d and repeatedly square it.
   If 'n' is prime, the sequence must either:
   1. Start with 1 (a^d ≡ 1)
   2. Hit -1 (n-1) at some point before reaching a^(n-1).

B) Why it beats Fermat:
   If the sequence hits 1 but the previous number was NOT -1, we have found a non-trivial 
   square root of 1. This mathematically proves 'n' is composite. This extra check 
   successfully identifies Carmichael numbers as composite, completely fixing Fermat's flaw.

C) Error Probability (Monte Carlo Algorithm):
   - A base 'a' that wrongly claims a composite number is prime is a "strong liar".
   - Theorem: For any composite number 'n', at most 1/4 of all possible bases are strong liars.
   - Therefore, the probability of a false positive for a single random base is ≤ 25%.
   - After 'k' independent iterations, the error probability drops exponentially to (1/4)^k.
   - For k = 10, the chance of a false positive is less than 1 in 1,048,576.

D) Complexity:
   - Time Complexity: O(k * log^3 n) bit operations, or O(k * log n) if we consider 
     multiplication as an O(1) operation for standard integer types.
   - Space Complexity: O(1) auxiliary space.
'''