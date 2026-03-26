
n = int(input())

col = set()
diag1 = set()
diag2 = set()

sol = [0] * n
total = 0
first = None

def back(r):
    global first, total

    if r == n:
        total += 1
        if first is None:
            first = sol.copy()
            return
        
    for c in range(1, n + 1):
        if c in col or (r + c) in diag1 or (r - c) in diag2:
            continue
        
        col.add(c)
        diag1.add(r + c)
        diag2.add(r - c)
        sol[r] = c
        back(r + 1)
        col.remove(c)
        diag1.remove(r + c)
        diag2.remove(r - c)
    
back(0)
print(*first)
print(total)

