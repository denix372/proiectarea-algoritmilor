# Dynamic programming approach

def longestPalindrome(s):
    n = len(s)
    if n <= 1:
        return s
    dp = [[False] * n for _ in range(n)]
    start = 0
    max_len = 1

    for i in range(n):
        dp[i][i] = True

    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_len = 2

    for lenght in range(3, n + 1):
        for i in range(n - lenght + 1):
            j = i + lenght - 1

            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                start = i
                max_len = lenght
    return s[start:start + max_len]

# Two Pointers / Expansion from center approach
def longestPalindrome2(s):
    if not s:
        return ""
    n = len(s)
    start = 0
    end = 0
    res = 0
    def expand(l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return l + 1, r - 1
    
    for i in range(n):
        l, r = i, i 
        while l >= 0 and r < n and s[l] == s[r]:
            if r - l + 1 > res:
                start = l
                end = r
                res = r - l + 1
            l -= 1
            r += 1

        l, r = i, i + 1
        while l >= 0 and r < n and s[l] == s[r]:
            if r - l + 1 > res:
                start = l
                end = r
                res = r - l + 1
            l -= 1
            r += 1

    return s[start: end + 1]
    
print(longestPalindrome("babad"))
print(longestPalindrome2("babad"))