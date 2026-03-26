


def gray_code(n):
    res =[]

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

n = int(input())
res = gray_code(n)
for r in res:
    print(r)