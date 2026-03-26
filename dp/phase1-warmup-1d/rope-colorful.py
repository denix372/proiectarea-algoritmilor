from typing import List
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(neededTime)
        i = 0
        total = 0

        while i < n - 1:
            j = i

            gr_sum = 0
            gr_max = 0

            while j < n and colors[j] == colors[i]:
                gr_sum += neededTime[j]
                gr_max = max(gr_max, neededTime[j])
                j += 1

            total += gr_sum - gr_max
            i = j
        return total
                
colors = "aabaa"
neededTime = [1,2,3,4,1]
sol = Solution()
print(sol.minCost(colors, neededTime))