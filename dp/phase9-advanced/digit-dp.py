from functools import cache

""" Given four integers a, b, d, and k, count how many numbers in the range
[a, b] contain the digit d exactly k times. """

from functools import cache

def solve(a, b, d, k):
    
    def count_digits(x):
        if x < 0:
            return 0
            
        s = str(x)
        
        @cache
        def dp(i, count, is_limit):
            if count > k:
                return 0
                
            if i == len(s):
                return 1 if count == k else 0
            
            ans = 0
            upper_bound = int(s[i]) if is_limit else 9
            
            for digit in range(upper_bound + 1):
                new_limit = is_limit and (digit == upper_bound)
                
                new_count = count + (1 if digit == d else 0)
            
                ans += dp(i + 1, new_count, new_limit)
                
            return ans

        return dp(0, 0, True)

    return count_digits(b) - count_digits(a - 1)


# Solution in O(d * k * 2 * 10)
def solve2(a, b, d, k):

    def count(x):
        if x < 0:
            return 0
        
        digits = list(map(int, str(x)))
        n = len(digits)
        # dp[i][cnt]: Ways to build a prefix of length 'i' with 'cnt' occurrences of 'd',
        # tight: where the prefix is EXACTLY matching the prefix of 'x'.
        # loose: where the prefix is STRICTLY LESS than the prefix of 'x'.
        dp_tight = [[0] * (k + 1) for _ in range(n + 1)]
        dp_loose = [[0] * (k + 1) for _ in range(n + 1)]

        dp_tight[0][0] = 1

        for i in range(n):
            for cnt in range(k + 1):
                if dp_tight[i][cnt] > 0:
                    for c in range(digits[i] + 1):
                        ncnt = cnt + (1 if c == d else 0) # next count
                        if ncnt > k:
                            continue
                        # If we pick the maximum allowed digit, we remain restricted (tight)
                        # else we break free from the limit (loose)
                        if c == digits[i]:
                            dp_tight[i + 1][ncnt] += dp_tight[i][cnt]
                        else:
                            dp_loose[i + 1][ncnt] += dp_tight[i][cnt]
                        
                if dp_loose[i][cnt] > 0:
                    for c in range(10):
                        ncnt = cnt + (1 if c == d else 0)
                        if ncnt > k:
                            continue

                        # Once we are loose, any digit we add keeps us in the loose state
                        dp_loose[i + 1][ncnt] += dp_loose[i][cnt]

        return dp_tight[n][k] + dp_loose[n][k]

    return count(b) - count(a - 1)

a = 100
b = 500
d = 3
k = 1
print(solve(a, b, d, k))
print(solve2(a, b, d, k))