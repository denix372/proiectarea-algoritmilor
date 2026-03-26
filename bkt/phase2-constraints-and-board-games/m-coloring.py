#Cheking validity
def valid(k, sol, adj):
    for v in adj[k]:
        if sol[v] == sol[k]:
            return False
    return True


def bkt(k, n, m, sol, adj):
    if k == n:
        return True

    for color in range(1, m+1):
        sol[k] = color
        if valid(k, sol, adj):
            if bkt(k + 1, n, m, sol, adj):
                return True
        sol[k] = 0

    return False


def bkt2(k, n, m, sol, adj, all_solutions):
    if k == n:
        all_solutions.append(sol.copy())
        return

    for color in range(1, m+1):
        sol[k] = color
        if valid(k, sol, adj):
            bkt2(k + 1, n, m, sol, adj, all_solutions)
        sol[k] = 0

n = 4
adj = [
    [1,2,3],   # 0
    [0,3],     # 1
    [0,3],     # 2
    [0,1,2]    # 3
]

m = 3
sol = [0] * n

print("Există colorare?", bkt(0, n, m, sol, adj))

all_solutions = []
bkt2(0, n, m, sol, adj, all_solutions)

print("Toate soluțiile:")
for s in all_solutions:
    print(s)
