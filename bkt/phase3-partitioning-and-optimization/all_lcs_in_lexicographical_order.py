def lcs(s1, s2, dp):
    m, n = len(s1), len(s2)

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if s1[i] == s2[j]:
                dp[i][j] = dp[i + 1][j + 1] + 1
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

def solve(s1, s2):
    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    lcs(s1, s2, dp)
    lcslen = dp[0][0]

    res = []
    sol = []
    
    def back(i, j, sol):
        if len(sol) == lcslen:
            res.append("".join(sol))
            return
        
        if i == len(s1) or j == len(s2):
            return
        
        len_sol = len(sol)

        for c in range(ord('a'), ord('z') + 1):
            char = chr(c)
            found = False

            for ki in range(i, len(s1)):
                if s1[ki] != char:
                    continue
                
                for kj in range(j, len(s2)):
                    if s2[kj] == char and dp[ki][kj] == lcslen - len_sol:
                        sol.append(char)
                        back(ki + 1, kj + 1, sol)
        
                        sol.pop()
                        found = True
                        break
                    if found:
                        break

    back(0, 0, sol)

    return res

s1 = "abac"
s2 = "aabca"

res = solve(s1, s2)

print("[", end="")
for i in range(len(res)):
    print(f"\"{res[i]}\"", end="")
    if i + 1 < len(res):
        print(", ", end="")
print("]")