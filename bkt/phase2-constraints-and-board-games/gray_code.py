def gray_code(n):
    if n == 1:
        return ["0", "1"]
    
    prev = gray_code(n - 1)
    rez = []

    for code in prev:
        rez.append("0" + code)

    for code in reversed(prev):
        rez.append("1" + code)

    return rez

def gray_code(n):
    res = []

    def back(k):
        if k == n:
            res.append("".join(sol))
            return

        back(k + 1)
        if sol[k] == '0':
            sol[k] = '1'
        else:
            sol[k] = '0'
        
        back(k + 1)
        
    sol = ["0"] * n
    back(0)
    return res


def gray_code2(n):
    rez = []
    for i in range(1 << n):  # 0 .. 2^n - 1
        g = i ^ (i >> 1)
        rez.append(format(g, f'0{n}b'))
    return rez

n = int(input())
for code in gray_code2(n):
    print(code)
