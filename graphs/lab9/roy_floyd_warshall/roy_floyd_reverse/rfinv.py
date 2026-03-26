INF = 10**15

def rfinv(n, D):
    # 1) Validare Floyd–Warshall invers
    for i in range(n):
        if D[i][i] != 0:
            return None

    for i in range(n):
        for j in range(n):
            if D[i][j] != D[j][i]:
                return None

    for k in range(n):
        for i in range(n):
            dik = D[i][k]
            for j in range(n):
                if D[i][j] > dik + D[k][j]:
                    return None

    # 2) Numărare muchii necesare
    cnt = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            needed = True
            for k in range(n):
                if k != i and k != j:
                    if D[i][j] == D[i][k] + D[k][j]:
                        needed = False
                        break
            if needed:
                cnt += 1

    return cnt

def solve():
    T = int(input())
    for _ in range(T):
        n, m = map(int, input().split())

        for _ in range(m):
            input()

        D = []
        for _ in range(n):
            D.append(list(map(int, input().split())))

        res = rfinv(n, D)
        if res is None:
            print("NU")
        else:
            print("DA", res)
solve()
