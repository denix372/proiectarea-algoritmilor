class Solution:
    def permutation(self, s):
        # code here
        dom = s
        res = []
        n = len(s)
        
        def bkt(sol, dom):
            if len(sol) == n:
                res.append(sol)
                return
            
            for i in range(len(dom)):
                new_sol = sol + dom[i]
                new_dom = dom[:i] + dom[i + 1:]
                bkt(new_sol, new_dom)
        bkt("", dom)
        return sorted(res)

s = "AA"
print(Solution().permutation(s))