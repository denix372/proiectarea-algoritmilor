def wordBreak(s, dictionary):
    word_set = set(dictionary)
    n = len(s)
    
    # dp[i] means: "Can the prefix of length i be segmented into dictionary words?"
    dp = [False] * (n + 1)
    
    # Base case: an empty string can always be segmented
    dp[0] = True 
    
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                # Trick 2: We only need ONE valid way to reach 'i', so we can stop checking 'j's
                break 
                
    return dp[n]

s = "ilike"
dictionary = ["i", "like", "gfg"]
print(wordBreak(s, dictionary))