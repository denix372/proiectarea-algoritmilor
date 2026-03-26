class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        dp = [[0] * (m + 1) for i in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = i
        for j in range(m + 1):
            dp[0][j] = j

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
        return dp[n][m]
        
#Optimization
def editDistance2(s1, s2):
    m = len(s1)
    n = len(s2)

    # Stores dp[i-1][j-1]
    prev = 0
    curr = [0] * (n + 1)

    for j in range(n + 1):
        curr[j] = j

    for i in range(1, m + 1):
        prev = curr[0]
        curr[0] = i
        for j in range(1, n + 1):
            temp = curr[j]
            if s1[i - 1] == s2[j - 1]:
                curr[j] = prev
            else:
                curr[j] = 1 + min(curr[j - 1], prev, curr[j])
            prev = temp

    return curr[n]

#Reconstruction
def reconstructEditDistance(word1, word2):
    n = len(word1)
    m = len(word2)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],     # delete
                    dp[i][j - 1],     # insert
                    dp[i - 1][j - 1]  # replace
                )

    ops = []
    i, j = n, m

    while i > 0 or j > 0:
        if i > 0 and j > 0 and word1[i-1] == word2[j-1]:
            ops.append(f"Match '{word1[i-1]}'")
            i -= 1
            j -= 1

        elif i > 0 and dp[i][j] == dp[i-1][j] + 1:
            ops.append(f"Delete '{word1[i-1]}'")
            i -= 1

        elif j > 0 and dp[i][j] == dp[i][j-1] + 1:
            ops.append(f"Insert '{word2[j-1]}'")
            j -= 1

        else:
            ops.append(f"Replace '{word1[i-1]}' with '{word2[j-1]}'")
            i -= 1
            j -= 1

    ops.reverse()
    return ops


sol = Solution()
word1 = "horse"
word2 = "ros"
print(sol.minDistance(word1, word2))
print(editDistance2(word1, word2))
print(reconstructEditDistance(word1, word2))