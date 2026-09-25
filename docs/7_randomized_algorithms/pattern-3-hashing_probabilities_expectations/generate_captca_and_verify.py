import random
import string

class CaptchaSystem:
    def __init__(self):
        # Character pool: a-z (26) + A-Z (26) + 0-9 (10) = 62 characters
        self.char_pool = string.ascii_letters + string.digits
        
    # Time Complexity: O(n) where n is the length of the CAPTCHA
    def generate_captcha(self, length: int = 9) -> str:
        # random.choices picks 'k' elements from the pool with replacement (uniform probability)
        # "".join() concatenates the list of characters into a single string
        captcha_chars = random.choices(self.char_pool, k=length)
        return "".join(captcha_chars)
        
    # Time Complexity: O(n) for string comparison
    def verify_captcha(self, generated_captcha: str, user_input: str) -> bool:
        # A real-world system might also add case-insensitivity or time-out limits,
        # but standard CAPTCHA requires an exact match.
        return generated_captcha == user_input

# --- DRIVER CODE (EXAMPLE USAGE) ---
system = CaptchaSystem()

print("--- Automated CAPTCHA System ---")
# Generate a CAPTCHA of length 9
current_captcha = system.generate_captcha(9)
print(f"System generated CAPTCHA: {current_captcha}")

# Simulate user inputs
user_attempt_1 = "wrong1234"
user_attempt_2 = current_captcha

print(f"\nUser enters: '{user_attempt_1}'")
if system.verify_captcha(current_captcha, user_attempt_1):
    print("Result: CAPTCHA Matched (Human verified)")
else:
    print("Result: CAPTCHA Not Matched (Bot detected)")

print(f"\nUser enters: '{user_attempt_2}'")
if system.verify_captcha(current_captcha, user_attempt_2):
    print("Result: CAPTCHA Matched (Human verified)")
else:
    print("Result: CAPTCHA Not Matched (Bot detected)")
print()

'''
PROBABILISTIC ANALYSIS & COMBINATORICS (CAPTCHA Security)

A) Core Mathematical Idea:
   The CAPTCHA generation relies on uniform random sampling with replacement.
   We have a pool of N distinct characters. For an alphanumeric CAPTCHA:
   N = 26 (lowercase) + 26 (uppercase) + 10 (digits) = 62 characters.

B) Combinatorics (Total Possibilities):
   If we generate a CAPTCHA of length 'k', each of the 'k' positions can be filled 
   by any of the N characters independently.
   Total unique CAPTCHAs = N^k.
   For a standard length of k = 9:
   Total = 62^9 = 13,537,086,546,263,552 (over 13.5 quadrillion combinations).

C) Security (Probability of a blind guess):
   The probability of a bot successfully guessing the exact CAPTCHA by blind 
   brute force on a single attempt is exactly 1 / N^k.
   P(Guess) = 1 / 13,537,086,546,263,552.
   This approaches zero, making it mathematically impossible to bypass via 
   random guessing without using Optical Character Recognition (OCR) to actually 
   "read" the visual representation.

D) Complexity:
   - Time Complexity: O(k) to generate 'k' characters and O(k) to compare them.
   - Space Complexity: O(k) to store the generated string.
'''