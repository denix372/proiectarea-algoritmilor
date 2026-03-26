n = int(input())
t1, t2 = map(int, input().split())

cols = set()
diag1 = set()
diag2 = set()

cols.add(t2)
cnt = 0

def back(r):
    global cnt

    if r == n:
        cnt += 1
        return
    if r == t1:
        back(r + 1)
        return
    
    for c in range(n):
        if c == t2:
            continue

        d1 = (r + c, r > t1 and r + c == t1 + t2)
        d2 = (r - c, r > t1 and r - c == t1 - t2)

        if c in cols or d1 in diag1 or d2 in diag2:
            continue

        cols.add(c)
        diag1.add(d1)
        diag2.add(d2)

        back(r + 1)
        cols.remove(c)
        diag1.remove(d1)
        diag2.remove(d2)

back(0)
print(cnt)      