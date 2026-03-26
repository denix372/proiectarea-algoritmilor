MOD = 10**9 + 7
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        
        MOD = 10**9 + 7
        
        dpa = [0] * n
        dpe = [0] * n
        dpi = [0] * n
        dpo = [0] * n
        dpu = [0] * n
        
        dpa[0] = dpe[0] = dpi[0] = dpo[0] = dpu[0] = 1
        
        for pos in range(1, n):
            dpa[pos] = (dpe[pos-1] + dpi[pos-1] + dpu[pos-1]) % MOD
            dpe[pos] = (dpa[pos-1] + dpi[pos-1]) % MOD
            dpi[pos] = (dpe[pos-1] + dpo[pos-1]) % MOD
            dpo[pos] = dpi[pos-1] % MOD
            dpu[pos] = (dpi[pos-1] + dpo[pos-1]) % MOD
        
        return (dpa[n-1] + dpe[n-1] + dpi[n-1] + dpo[n-1] + dpu[n-1]) % MOD

print(Solution().countVowelPermutation(5))