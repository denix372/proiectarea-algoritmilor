from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []

        for i, v in enumerate(temperatures):
            while stack and stack[-1][1] < v:
                j, w = stack.pop()
                res[j] = (i - j)

            stack.append((i, v))

        return res

temperatures = [73,74,75,71,69,72,76,73]
print(Solution().dailyTemperatures(temperatures))