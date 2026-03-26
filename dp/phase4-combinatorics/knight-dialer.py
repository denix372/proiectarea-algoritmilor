MOD = 10**9 + 7
class Solution:
    def knightDialer(self, n: int) -> int:
        moves = {
            0: [4,6],
            1: [6,8],
            2: [7,9],
            3: [4,8],
            4: [0,3,9],
            5: [],       # 5 nu are vecini
            6: [0,1,7],
            7: [2,6],
            8: [1,3],
            9: [2,4]
        }
        dp = [[0] * 10 for _ in range(n)]
        for d in range(10):
                dp[0][d] = 1

        for i in range(1, n):
            for digit in range(10):
                for nxt in moves[digit]:
                    dp[i][nxt] = (dp[i][nxt] + dp[i - 1][digit]) % MOD
        return sum(dp[n - 1]) % MOD

        
n = 3131
sol = Solution()
print(sol.knightDialer(n))