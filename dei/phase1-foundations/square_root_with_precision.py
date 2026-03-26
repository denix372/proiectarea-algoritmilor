def squareRoot(n, e):
    left, right = 0, n
    while right - left > e:
        mid = (left + right) / 2.0
        if mid * mid < n:
            left = mid
        else:
            right = mid
    return right

n = 50
e = 0.001
p = 3
print(f"{squareRoot(n, e):.{p}f}")