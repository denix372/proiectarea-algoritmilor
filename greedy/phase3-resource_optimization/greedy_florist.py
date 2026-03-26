

def solve(n, k, c):
    c.sort(reverse = True)
    res = 0
    i = 0
    while i < n:
        for j in range(k):
            if j + i * k >= n:
                break
            res += (i + 1) * c[j + i * k]
        i += 1
    return res
    

k = 3
c = [1, 3, 5, 7, 9]
print(solve(len(c), k, c))

