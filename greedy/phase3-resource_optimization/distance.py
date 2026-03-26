

def solve(n, m, d):
    refills = 0
    i = 0

    while i < n - 1:
        j = i
        while i < n - 1 and d[i + 1] - d[j] <= m:
            i += 1

        if i == j:
            return -1

        if i < n - 1:
            refills +=1
    return refills


n = 5
m = 10
d = [2, 8, 15, 25, 30]
print(solve(len(d), m, d))