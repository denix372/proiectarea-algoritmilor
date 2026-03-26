class Solution:
    def distinctSum(self, arr):
        # code here
        s = sum(arr)
        dp =[False] * (s + 1)
        res = [0]
        dp[0] = True
        for num in arr:
            for j in range(s, num - 1, -1):
                if j - num >= 0:
                    dp[j] = dp[j] or dp[j - num] 
    
        for j in range(1, s + 1):
            if dp[j]:
                res.append(j)
    
        return res

arr = [1, 2, 3]
print(Solution().distinctSum(arr))