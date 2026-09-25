from collections import defaultdict
class Solution:
    def is_isomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d = defaultdict(chr)
        used = set()

        for x, y in zip(s, t):
            if x not in d:
                if y in used:
                    return False
                d[x] = y
                used.add(y)
            elif d[x] != y:
                return False
        return True
s = "egg"
t = "add"
print(Solution().isIsomorphic(s, t))