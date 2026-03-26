
def solve(n, edges):
    if len(edges) != n - 1:
        return False

    parent = [i for i in range(n)]
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    for u, v in edges:
        ru = find(u)
        rv = find(v)

        if ru == rv:
            return False
    
        
        parent[ru] = rv

    return True

n = 5
edges = [[0,1], [0,2], [0,3], [1,4]]
print(solve(n, edges))