class RabinKarp:
    def __init__(self, base: int = 31, mod: int = 10**9 + 7):
        # Base (B): Usually 31 for lowercase English letters, or 256 for extended ASCII
        # Mod (M): A large prime number to avoid integer overflow and minimize collisions
        self.B = base
        self.MOD = mod

    def search(self, pattern: str, text: str) -> list[int]:
        M = len(pattern)
        N = len(text)
        
        if M == 0 or N == 0 or M > N:
            return []

        # 1. Calculate B^(M-1) % MOD (The multiplier for the most significant character)
        highest_pow = 1
        for _ in range(M - 1):
            highest_pow = (highest_pow * self.B) % self.MOD
            
        p_hash = 0  # Hash for the pattern
        t_hash = 0  # Hash for the current window of text
        
        # 2. Compute the initial hashes for the pattern and the first window of the text
        for i in range(M):
            p_hash = (p_hash * self.B + ord(pattern[i])) % self.MOD
            t_hash = (t_hash * self.B + ord(text[i])) % self.MOD
            
        occurrences = []
        
        # 3. Slide the pattern over the text one by one
        for i in range(N - M + 1):
            
            # If the hash values match, we found a potential match
            if p_hash == t_hash:
                # Las Vegas approach: verify character by character to rule out collisions
                if text[i : i + M] == pattern:
                    occurrences.append(i)
                    
            # 4. Calculate the hash for the NEXT window (Rolling Hash technique)
            if i < N - M:
                # Formula: new_hash = (old_hash - text[i] * B^(M-1)) * B + text[i+M]
                t_hash = (t_hash - ord(text[i]) * highest_pow) % self.MOD
                t_hash = (t_hash * self.B + ord(text[i + M])) % self.MOD
                
                # In some languages (like C++/Java), modulo of a negative number is negative.
                # Python handles this gracefully, but adding self.MOD is a robust best practice.
                t_hash = (t_hash + self.MOD) % self.MOD
                
        return occurrences

# --- DRIVER CODE (EXAMPLE USAGE) ---
rk = RabinKarp()
text = "geeksforgeeks is a computer science portal for geeks"
pattern = "geeks"

print("--- Rabin-Karp String Matching ---")
print(f"Text: '{text}'")
print(f"Pattern: '{pattern}'")
matches = rk.search(pattern, text)
print("Pattern found at indices:", matches)
print()

'''
PROBABILISTIC ANALYSIS & PROOF (Polynomial Rolling Hash & Rabin-Karp)

A) Core Mathematical Idea (Polynomial Hash):
   We treat a string as a number written in base B. 
   Hash(S) = (S[0]*B^(M-1) + S[1]*B^(M-2) + ... + S[M-1]*B^0) % MOD.
   By keeping MOD as a large prime, we map strings to integers uniformly, 
   enabling O(1) comparison between two strings.

B) The "Rolling" Property (O(1) Window Sliding):
   To slide the window one character to the right (from index i to i+1), we must:
   1. Remove the contribution of the leftmost character: Hash = Hash - text[i] * B^(M-1)
   2. Shift all remaining characters one position left (multiply by B): Hash = Hash * B
   3. Add the new rightmost character: Hash = Hash + text[i+M]
   4. Apply modulo at each step.
   This O(1) transformation is what makes Rabin-Karp so powerful, avoiding the 
   recalculation of the hash from scratch (which would take O(M)).

C) Classification (Las Vegas Algorithm):
   Because the hash space is finite [0, MOD-1], two different strings can produce 
   the exact same hash (a collision).
   - If we strictly trust the hash and return true on a match, it's a Monte Carlo 
     algorithm (fast, but small chance of false positive).
   - If we verify the string character-by-character whenever hashes match (as implemented 
     above with 'text[i:i+M] == pattern'), it becomes a Las Vegas algorithm. The result 
     is guaranteed 100% correct, but the execution time might vary if collisions occur.

D) Complexity:
   - Average/Best Time Complexity: O(N + M). The hashes are calculated once for 
     the pattern and first window O(M), and then the window slides N-M times in O(1).
   - Worst Time Complexity: O(N * M). This happens if the hash generates an extreme 
     number of collisions (e.g., searching for "AAA" in "AAAAAAA"), forcing the 
     Las Vegas string verification to run constantly.
   - Space Complexity: O(1) auxiliary space.
'''