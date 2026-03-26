# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

def isBadVersion(version: int) -> bool:
    return version >= bad

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2
            if not isBadVersion(mid):
                left = mid + 1
            elif isBadVersion(right):
                right = mid - 1
            else:
                left = mid + 1

        return left

n = 5
bad = 4
print(Solution().firstBadVersion(n))