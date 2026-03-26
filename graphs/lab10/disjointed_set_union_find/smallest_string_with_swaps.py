from collections import defaultdict

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: list[list[int]]) -> str:
        n = len(s)
        parent = [i for i in range(n)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        for u, v in pairs:
            ru = find(u)
            rv = find(v)
            if ru != rv:
                parent[ru] = rv
        
        groups = defaultdict(list)
        for i in range(n):
            root = find(i)
            groups[root].append(s[i])
        
        for root in groups:
            groups[root].sort(reverse = True)
        
        res = []
        for i in range(n):
            root = find(i)
            res.append(groups[root].pop())
        
        return "".join(res)

s = "dcab"
pairs = [[0,3],[1,2]]
print(Solution().smallestStringWithSwaps(s, pairs))