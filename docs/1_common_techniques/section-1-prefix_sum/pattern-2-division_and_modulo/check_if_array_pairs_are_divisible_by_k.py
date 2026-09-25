from collections import defaultdict

class Solution:
    def can_arrange(self, arr: list[int], k: int) -> bool:
        d = defaultdict(int)
        for x in arr:
            d[x % k] += 1
        
        for r in d:
            if r == 0:
                if d[r] % 2 != 0:
                    return False
            else:
                if d[r] != d[k - r]:
                    return False

        return True

arr = [1,2,3,4,5,10,6,7,8,9]
k = 5
print(Solution().canArrange(arr, k))
