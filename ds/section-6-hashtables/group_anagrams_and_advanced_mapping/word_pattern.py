from collections import defaultdict

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(pattern) != len(s.split()):
            return False
        d = defaultdict(list)
        used = set()
        for x, y in zip(pattern, s.split()):
            if x not in d:
                if y in used:
                    return False
                d[x] = y
                used.add(y)
            elif d[x] != y:
                return False
        return True

pattern = "abba"
s = "dog cat cat dog"
print(Solution().wordPattern(pattern, s))