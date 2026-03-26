class Solution:
    def arrangeCoins(self, n: int) -> int:
        left = 0
        right = n
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            if mid * (mid + 1) // 2 <= n:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
        
print(Solution().arrangeCoins(8))