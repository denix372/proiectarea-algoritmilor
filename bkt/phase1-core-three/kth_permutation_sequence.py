class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        res = []
        cnt = 0
        dom = "".join(map(str, list(range(1, n + 1))))

        def bkt(sol, dom):
            nonlocal cnt
            if len(sol) >= n:
                cnt += 1
                if cnt == k:
                    return sol
                res.append(sol)
                return

            for i in range(len(dom)):
                new_sol = sol + dom[i]
                new_dom = dom[:i] + dom[i + 1:]
                ans = bkt(new_sol, new_dom)
                if ans:
                    return ans
            return None

        return bkt("", dom)
n = 3
k = 3
print(Solution().getPermutation(n, k))