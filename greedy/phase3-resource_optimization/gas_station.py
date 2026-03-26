from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        if sum(gas) < sum(cost):
            return -1

        total = 0
        res = 0
        for i in range(n):
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                res = i + 1
        return res

gas = [1,2,3,4,5]
cost = [3,4,5,1,2]

print(Solution().canCompleteCircuit(gas, cost))