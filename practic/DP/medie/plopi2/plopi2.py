
def solve(n, v):
    m = v[0]
    s = 0
    cnt = 0
    for i in range(1, n):
        if v[i] > m:
            s += v[i] - m
            cnt += 1
        else:
            m = v[i]

    with open("plopi2.out", "w") as fout:
        fout.write(str(cnt) + " " + str(s))


with open("plopi2.in", "r") as fin:
    n = int(fin.readline())
    v = list(map(int, fin.readline().split()))

solve(n, v)
