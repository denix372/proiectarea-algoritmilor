class Solution:
    def permute(self, nums):
        res = []
        n = len(nums)
        def back(domain, sol):
            if (len(sol) == n):
                res.append(sol.copy())
                return

            for i in range(len(domain)):
                new_sol = sol.copy()
                new_domain = domain.copy()

                new_sol.append(domain[i])
                new_domain.pop(i)

                back(new_domain, new_sol)

        back(nums, [])
        return res
    

def permute2(domain, used, solution):
    if len(domain) == len(solution):
        print(solution)
        return

    for i in range(len(domain)):
        if not used[i]:
            used[i] = True
            #new_solution = solution.copy()
            #new_domain = domain.copy()
            
            solution.append(domain[i])
        
            permute2(domain, used,  solution)

            solution.pop()
            used[i] = False #?


print("-----normal permutations------")
sol = Solution()
for i in sol.permute([1, 2, 3]):
    print(i)


print("-----permutations with an array------")
nums = [4, 5, 6]
used = [False] * len(nums)
permute2([4, 5, 6], used, [])
