def k_permutations(nums, k):
    res = []
    n = len(nums)
    def back(domain, sol):
        if (len(sol) == k):
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


for i in k_permutations([1, 2, 3], 2):
    print(i)