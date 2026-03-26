# regular LIS O(n^2) (gives TLE)
def longestSubseq_lis(self, arr):
    # code here
    n = len(arr)
    if n == 0:
        return 0
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if abs(arr[i] - arr[j]) == 1:
                dp[i] = max(dp[i], dp[j] + 1)
                
    return max(dp)

# O(n) solution
class Solution:
    def longestSubseq(self, arr):
        dp = {}
        max_len = 0
        
        for num in arr:
            dp[num] = max(dp.get(num - 1, 0), dp.get(num + 1, 0)) + 1
            if dp[num] > max_len:
                max_len = dp[num]
                
        return max_len

arr = [10, 9, 4, 5, 4, 8, 6]
print(Solution().longestSubseq(arr))