class Solution:
    def combine(self, n: int, k: int):
        res = []
        def back(sol, index):
            if (len(sol) == k):
                res.append(sol.copy())
                return

            for i in range(index, n + 1): 
                sol.append(i)
                back(sol, i + 1)
                sol.pop()

        back( [], 1)
        return res


sol = Solution()
for i in sol.combine(4, 2):
    print(i)