from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        sol = []
        def back(openN, closeN):
            if openN == closeN == n:
                res.append("".join(sol))
                return

            if openN < n:
                sol.append("(")
                back(openN + 1, closeN)
                sol.pop()

            if closeN < openN:
                sol.append(")")
                back(openN, closeN + 1)
                sol.pop()


        back(0, 0)
        return res
        
sol = Solution()
for i in sol.generateParenthesis(3):
    print(i)