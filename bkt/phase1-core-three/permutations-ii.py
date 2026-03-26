from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        
        def back(domain, sol):
            if len(sol) == n:
                res.append(sol.copy())
                return
            
            i = 0
            while i < len(domain):

                new_sol = sol.copy()
                new_domain = domain.copy()

                while i + 1 < len(domain) and domain[i] == domain[i + 1]:
                    i += 1

                new_sol.append(domain[i])
                new_domain.pop(i)
                back(new_domain, new_sol)
                i += 1

        back(nums, [])
        return res

sol = Solution()
for i in sol.permuteUnique([1, 2, 2, 1]):
    print(i)