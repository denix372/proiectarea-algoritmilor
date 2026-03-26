from typing import List
from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        
        def isValid(st):
            count = 0
            for c in st:
                if c == '(':
                    count += 1
                elif c == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        res = []
        visited = set([s])
        q = deque([s])
        found = False

        while q:
            cur = q.popleft()

            if isValid(cur):
                res.append(cur)
                found = True

            if found:
                # don't generate on the next level
                continue

            for i in range(len(cur)):
                if cur[i] not in "()":
                    continue
                nxt = cur[:i] + cur[i+1:]
                if nxt not in visited:
                    visited.add(nxt)
                    q.append(nxt)

        return res
s = "()())()"
sol = Solution()
print(sol.removeInvalidParentheses(s))