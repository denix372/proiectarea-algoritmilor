
def connecting_cities_with_minimum_cost(n: int, connections: list[list[int]]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    def find(x):
        if parent[x] != x: 
            parent[x] = find(parent[x]) #path compression
        return parent[x]

    def union(a, b):
        ra = find(a)
        rb = find(b)
        if ra == rb:
            return False
        if rank[ra] < rank[rb]:
            parent[ra] = rb
        elif rank[ra] > rank[rb]:
            parent[rb] = ra
        else:
            parent[rb] = ra
            rank[ra] += 1
        return True        

    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    cnt = 0
    cost = 0

    connections.sort(key = lambda x : x[2])

    for u, v, w in connections:
        if union(u, v):
            cost += w
            cnt += 1
            if cnt == n - 1:
                break
    if cnt != n - 1:
        return -1
    return cost

n = 3
connections =  [[1,2,5], [1,3,6], [2,3,1]]
print(connecting_cities_with_minimum_cost(3, connections))