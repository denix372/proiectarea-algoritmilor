
def longCommSubstr(s1, s2):
    n = len(s1)
    m = len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    res = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                res = max(res, dp[i][j])
            else:
                dp[i][j] = 0
    return res

def longCommSubstrReconstrut(s1, s2):
    n = len(s1)
    m = len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    res = 0
    end = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if res < dp[i][j]:
                    res = dp[i][j]
                    end = i
            else:
                dp[i][j] = 0
    return s1[end - res: end]

#Optimized

def longCommSubstr2(s1, s2):
    n = len(s1)
    m = len(s2)

    # Create a 1D array to store the previous row's results
    prev = [0] * (m + 1)
    
    res = 0
    for i in range(1, n + 1):
      
        # Create a temporary array to store the current row
        curr = [0] * (m + 1)
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                curr[j] = prev[j - 1] + 1
                res = max(res, curr[j])
            else:
                curr[j] = 0
        
        # Move the current row's data to the previous row
        prev = curr
    
    return res


text1 = "abcde"
text2 = "acde" 

print(longCommSubstr2(text1, text2))
print(longCommSubstrReconstrut(text1, text2))