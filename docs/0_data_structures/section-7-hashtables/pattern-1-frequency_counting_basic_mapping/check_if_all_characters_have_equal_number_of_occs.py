from collections import defaultdict

class Solution:
    def are_occurrences_equal(self, s: str) -> bool:
        d = defaultdict(int)
        for x in s:
            d[x] += 1
        prove = d[s[0]]
        return all(x == prove for x in d.values())
s = "abacbc"
print(Solution().areOccurrencesEqual(s))