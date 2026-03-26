from collections import deque

def nqueens_ac3(n):
    # Variables are Q1, Q2, ..., Qn (represented as 0..n-1)
    variables = list(range(n))

    # Domains: each queen can be placed in any column 0..n-1
    domains = {i: set(range(n)) for i in variables}

    # Constraint: Qi and Qj cannot attack each other
    def constraint(i, vi, j, vj):
        if vi == vj:  # same column
            return False
        if abs(vi - vj) == abs(i - j):  # same diagonal
            return False
        return True

    # Build all arcs (Qi, Qj)
    queue = deque()
    for i in variables:
        for j in variables:
            if i != j:
                queue.append((i, j))

    # revise(i, j): remove values from D(i) that have no support in D(j)
    def revise(i, j):
        removed = False
        to_remove = set()

        for vi in domains[i]:
            supported = False
            for vj in domains[j]:
                if constraint(i, vi, j, vj):
                    supported = True
                    break
            if not supported:
                to_remove.add(vi)

        if to_remove:
            domains[i] -= to_remove
            removed = True

        return removed

    # AC-3 main loop
    while queue:
        i, j = queue.popleft()

        if revise(i, j):
            if not domains[i]:
                return None  # domain wipe-out → inconsistent CSP

            # If something was removed, re-add neighboring arcs
            for k in variables:
                if k != i and k != j:
                    queue.append((k, i))

    return domains


# Example: N = 4
domains = nqueens_ac3(4)
print(domains)
