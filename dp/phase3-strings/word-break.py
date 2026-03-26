def wordBreak(s, dictionary):
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for w in dictionary:
            # Check if current word is present
            # the prefix before the word is also breakable
            start = i - len(w)
            if start >= 0 and dp[start] and s[start:start +len(w)] == w:
                dp[i] = True
                break
    return dp[n]

s = "ilike"
dictionary = ["i", "like", "gfg"]
print(wordBreak(s, dictionary))