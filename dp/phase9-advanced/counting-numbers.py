from functools import cache

def solve(a, b):
    
    def count_valid_numbers(x):
        if x < 0:
            return 0
            
        s = str(x)
        @cache
        def dp(i, prev_digit, is_limit, is_lead_zero):
            if i == len(s):
                return 1
                
            ans = 0
            upper_bound = int(s[i]) if is_limit else 9

            for digit in range(upper_bound + 1):
                new_limit = is_limit and (digit == upper_bound)
                
                if is_lead_zero and digit == 0:
                    ans += dp(i + 1, -1, new_limit, True)
                else:
                    if digit != prev_digit:
                        ans += dp(i + 1, digit, new_limit, False) 
            return ans

        return dp(0, -1, True, True)

    return count_valid_numbers(b) - count_valid_numbers(a - 1)

def solve2(a, b):

    def count(x):
        if x < 0:
            return 0
            
        digits = list(map(int, str(x)))
        n = len(digits)

        dp_tight = [[0] * 11 for _ in range(n + 1)]
        dp_loose = [[0] * 11 for _ in range(n + 1)]
        
        dp_tight[0][10] = 1
        
        for i in range(n):
            limit = digits[i]
            
            for j in range(11):
                if dp_tight[i][j] > 0:
                    for c in range(limit + 1):
                        if j != 10 and c == j:
                            continue

                        # If we place a 0 during leading zeros, we stay in leading zeros (10)
                        nj = 10 if (j == 10 and c == 0) else c
                        
                        if c == limit:
                            dp_tight[i + 1][nj] += dp_tight[i][j]
                        else:
                            dp_loose[i + 1][nj] += dp_tight[i][j]
        
                if dp_loose[i][j] > 0:
                    for c in range(10):
                        if j != 10 and c == j:
                            continue
                            
                        nj = 10 if (j == 10 and c == 0) else c
                        dp_loose[i + 1][nj] += dp_loose[i][j]
                        
        return sum(dp_tight[n]) + sum(dp_loose[n])

    return count(b) - count(a - 1)

a, b = map(int, input().split())
print(solve(a, b))