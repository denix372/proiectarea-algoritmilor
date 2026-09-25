from typing import List

# Mock class provided by LeetCode (you don't submit this part)
class Master:
    def __init__(self, secret: str):
        self.secret = secret
        self.guesses = 0
        
    def guess(self, word: str) -> int:
        self.guesses += 1
        return sum(c1 == c2 for c1, c2 in zip(self.secret, word))

# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def find_secret_word(self, words: List[str], master: 'Master') -> None:
        def get_matches(w1: str, w2: str) -> int:
            return sum(c1 == c2 for c1, c2 in zip(w1, w2))

        candidates = words[:]
        for _ in range(30):
            best_word = ""
            min_worst_case_size = float('inf')
            
            # 1. MINIMAX LOGIC: Evaluate every candidate word
            for word in candidates:
                # Array to count how many words fall into each match-score bucket (0 to 6)
                score_buckets = [0] * 7
                
                for other in candidates:
                    if word != other:
                        score = get_matches(word, other)
                        score_buckets[score] += 1
                
                # The "Maximum Loss" is the largest bucket. If the API returns the score 
                # corresponding to this bucket, we are left with the most candidates.
                worst_case_size = max(score_buckets)
                
                # We want to "Minimize" this maximum loss
                if worst_case_size < min_worst_case_size:
                    min_worst_case_size = worst_case_size
                    best_word = word
                    
            # 2. Make the guess with our optimal word
            matches = master.guess(best_word)
            
            if matches == 6:
                return # Secret word found!
                
            # 3. Filter candidates: the secret word MUST have the exact same 
            # number of matches with 'best_word' as the API returned.
            candidates = [w for w in candidates if get_matches(w, best_word) == matches]

secret = "acckzz"
words = ["acckzz", "ccbazz", "eiowzz", "abcczz", "aaaaaa", "bbbbbb"]

master = Master(secret)
Solution().findSecretWord(words, master)

print("--- Guess the Word (Minimax) ---")
print(f"Secret Word: {secret}")
if master.guesses <= 10 and master.guess(secret) == 6:
    print(f"Result: You guessed the secret word correctly in {master.guesses - 1} tries!")
else:
    print("Result: Failed to find the word.")
print()

'''
GAME THEORY ANALYSIS & PROOF (Minimax Optimization)

A) Core Mathematical Idea (The Mastermind Strategy):
   At any point, we have a pool of valid candidate words. If we guess a word 'W', 
   the API returns a score 'C' (0 to 6). Based on 'C', we filter our pool to keep 
   only words that share exactly 'C' characters with 'W'.
   Our goal is to shrink the candidate pool as fast as possible. 

B) The Minimax Approach:
   For a given guess 'W', the remaining pool size strictly depends on the score 'C' 
   the API returns. The adversarial API (or just worst-case luck) will return the 
   score 'C' that corresponds to the largest subset of remaining words.
   - Let S(W, C) be the number of remaining candidates if we guess W and get score C.
   - The worst-case remaining size for guessing W is: Max_Loss(W) = max(S(W, C)) for C in 0..6.
   - To play optimally, we select the word W that minimizes this maximum loss:
     Best_W = argmin(Max_Loss(W)).

C) Why not just pick a random word?
   Picking a random word works fairly well on average because the distribution of 
   matches is heavily skewed towards 0 (most words share 0 letters). However, a 
   purely random approach has a mathematical probability of exceeding 10 guesses 
   in edge cases. The Minimax approach mathematically guarantees the most balanced 
   tree split at every step, safely keeping the depth under 10.

D) Complexity:
   - Time Complexity: O(N^2 * L), where N is the number of candidates and L is 
     the word length (6). Initially, N=100, so 100^2 * 6 = 60,000 operations per 
     guess, which is extremely fast. The pool drastically shrinks after the first guess.
   - Space Complexity: O(N) to store the filtered candidates list.
'''