from typing import List
from collections import defaultdict

class Solution:
    def group_the_people(self, groupSizes: List[int]) -> List[List[int]]:
        d = defaultdict(list)
        for i in range(len(groupSizes)):
            d[groupSizes[i]].append(i)
        res = []
        for i, v in d.items():
            sol = []
            for j in range(0, len(v), i):
                sol.append(v[j : j + i]) # group values chunk by chunk of size key
            res += sol
        return res
groupSizes = [3,3,3,3,3,1,3]
print(Solution().groupThePeople(groupSizes))