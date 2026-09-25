
class Solution:
    def smallest_equivalent_string(self, s1: str, s2: str, baseStr: str) -> str:
        parent = {chr(i): chr(i) for i in range(97, 123)}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(u, v):
            ru = find(u)
            rv = find(v)
            if ru != rv:
                if ru < rv:
                    parent[rv] = ru
                else:
                    parent[ru] = rv
        
        for i in range(len(s1)):
            union(s1[i], s2[i])
            
        res = []
        for char in baseStr:
            res.append(find(char))

        return "".join(res)

s1 = "parker"
s2 = "morris"
baseStr = "parser"
print(Solution().smallestEquivalentString(s1, s2, baseStr))