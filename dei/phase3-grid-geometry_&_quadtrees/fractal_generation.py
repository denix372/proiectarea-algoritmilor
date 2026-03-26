def hilbert_index(n, x, y):
    res = 0
    s = 1 << (n - 1)

    while s > 0:
        rx = 1 if (x & s) else 0
        ry = 1 if (y & s) else 0

        res += s * s * ((3 * rx) ^ ry)

        if ry == 0:
            if rx == 1:
                x = (1 << n) - 1 - x
                y = (1 << n) - 1 - y
            x, y = y, x

        s >>= 1

    return res

K, x, y = map(int, input().split())
print(hilbert_index(K, x - 1, y - 1))
