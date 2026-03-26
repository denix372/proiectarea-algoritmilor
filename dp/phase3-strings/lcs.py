# Longest Common Subsequence 

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[0] * (m + 1) for i in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i -1][j], dp[i][j - 1])
        return dp[n][m]
    
# Optimized
def longestCommonSubsequenceOptimized(text1, text2):
    if len(text1) > len(text2):
        text1, text2 = text2, text1

    n, m = len(text1), len(text2)
    prev = [0] * (n + 1)
    cur = [0] * (n + 1)

    for j in range(1, m + 1):
        for i in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                cur[i] = 1 + prev[i - 1]
            else:
                cur[i] = max(prev[i], cur[i - 1])
        prev, cur = cur, prev  # swap

    return prev[n]

#Reconstruction
def longestCommonSubsequenceReconstruct(text1, text2):
        n = len(text1)
        m = len(text2)
        dp = [[0] * (m + 1) for i in range(n + 1)]
        p = [[-1] * (m + 1) for i in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i -1][j], dp[i][j - 1])
    
        path = []
        i, j = n, m
        
        while i > 0 and j > 0:
            if text1[i - 1] == text2[j - 1]:
                path.append(text1[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] >= dp[i][j - 1]:
                i -= 1
            else:
                j -= 1

        path.reverse()
        return "".join(path)
        
    
text1 = "abcde"
text2 = "ace" 
sol = Solution()
print(sol.longestCommonSubsequence(text1, text2))
print(longestCommonSubsequenceOptimized(text1, text2))
print(longestCommonSubsequenceReconstruct(text1, text2))