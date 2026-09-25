
class Solution:
    def equations_possible(self, equations: list[str]) -> bool:
        parent = {chr(i): chr(i) for i in range(97, 123)}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        for eq in equations:
            if eq[1] == '=':
                ru = find(eq[0])
                rv = find(eq[3])

                parent[ru] = rv
        
        for eq in equations:
            if eq[1] == '!':
                if find(eq[0]) == find(eq[3]):
                    return False
        
        return True
            
equations = ["a==b","b!=a"]
print(Solution().equationsPossible(equations))