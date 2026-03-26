
from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        d = defaultdict(int)
        j = 0
        res = 0
        for i in range(len(fruits)):
            d[fruits[i]] += 1

            while len(d) > 2:
                d[fruits[j]] -= 1
                if d[fruits[j]] == 0:
                    del d[fruits[j]]
                j += 1

            res = max(res, i - j + 1)
        
        return res

fruits = [1,2,1]
print(Solution().totalFruit(fruits))