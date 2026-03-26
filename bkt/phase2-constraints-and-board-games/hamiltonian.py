def valid(k, sol, adj, n):
    # trebuie să fie vecin cu nodul anterior
    if sol[k] not in adj[sol[k-1]]:
        return False

    # nu trebuie să fie deja folosit
    for i in range(k):
        if sol[i] == sol[k]:
            return False

    return True


def hamiltonian(k, n, sol, adj):
    if k == n:am
        # verificăm dacă ultimul nod se leagă la primul
        return sol[n-1] in adj[sol[0]]

    for v in range(1, n):   # nodurile candidate
        sol[k] = v
        if valid(k, sol, adj, n):
            if hamiltonian(k + 1, n, sol, adj):
                return True
        sol[k] = -1

    return False

n = 4
adj = [
    [1,2],     # 0
    [0,2,3],   # 1
    [0,1,3],   # 2
    [1,2]      # 3
]

sol = [-1] * n
sol[0] = 0   # fixăm nodul de start

if hamiltonian(1, n, sol, adj):
    print("Ciclu hamiltonian găsit:", sol)
else:
    print("Nu există ciclu hamiltonian")
