import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline


def solve_giant_pizza(n, m, clauses):
    # Construim graful de implicații
    adj = [[] for _ in range(2*m)]

    def parse_literal(token1, token2=None):
        if token2 is None:
            sign = 1 if token1[0] == '+' else -1
            return sign * int(token1[1:])
        else:
            sign = 1 if token1 == '+' else -1
            return sign * int(token2)

    def var_index(x):
        v = abs(x) - 1
        return 2*v if x > 0 else 2*v + 1

    def neg(idx):
        return idx ^ 1

    # Construim muchiile
    for parts in clauses:
        if len(parts) == 2:
            s1, s2 = parts
            x1 = parse_literal(s1)
            x2 = parse_literal(s2)
        else:
            s1, n1, s2, n2 = parts
            x1 = parse_literal(s1, n1)
            x2 = parse_literal(s2, n2)

        a = var_index(x1)
        b = var_index(x2)
        na = neg(a)
        nb = neg(b)

        adj[na].append(b)
        adj[nb].append(a)

    # ---------- TARJAN SCC ----------
    n_nodes = 2*m
    disc = [-1] * n_nodes
    low = [-1] * n_nodes
    in_stack = [False] * n_nodes
    stack = []
    timer = [0]
    comp_id = [-1] * n_nodes
    sccs = []

    def dfs(u):
        timer[0] += 1
        disc[u] = low[u] = timer[0]
        stack.append(u)
        in_stack[u] = True

        for v in adj[u]:
            if disc[v] == -1:
                dfs(v)
                low[u] = min(low[u], low[v])
            elif in_stack[v]:
                low[u] = min(low[u], disc[v])

        if low[u] == disc[u]:
            comp = []
            while True:
                x = stack.pop()
                in_stack[x] = False
                comp.append(x)
                if x == u:
                    break
            sccs.append(comp)

    for i in range(n_nodes):
        if disc[i] == -1:
            dfs(i)

    # Atribuim ID‑urile SCC‑urilor în ordinea corectă (reversed)
    for idx, comp in enumerate(reversed(sccs)):
        for node in comp:
            comp_id[node] = idx

    # Verificăm contradicțiile
    for i in range(m):
        if comp_id[2*i] == comp_id[2*i + 1]:
            return "IMPOSSIBLE"

    # Construim soluția
    res = []
    for i in range(m):
        if comp_id[2*i] > comp_id[2*i + 1]:
            res.append('+')
        else:
            res.append('-')

    return ''.join(res)


# -------------------------
# INPUT / OUTPUT EXTERIOR
# -------------------------

n, m = map(int, input().split())
clauses = [input().split() for _ in range(n)]

print(solve_giant_pizza(n, m, clauses))
