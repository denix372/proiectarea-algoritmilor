

def semnal(n, a):
    max_ops = sum(a)

    min_ops = 0
    i = 0
    while i < n:
        if a[i] == 1:
            min_ops += 1
            i += 3
        else:
            i += 1
    return min_ops, max_ops

n = int(input())
a = list(map(int, input().split()))

x, y = semnal(n, a)
print(x, y)