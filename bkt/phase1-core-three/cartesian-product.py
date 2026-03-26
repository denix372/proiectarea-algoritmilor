def cartesian_product(domain):
    res = []
    n = len(domain)
    sol = []

    def back(index):
        if index == n:
            res.append(sol.copy())
            return

        for x in domain[index]:
            sol.append(x)
            back(index + 1)
            sol.pop()

    back(0)
    return res

domain = [
    [1, 2],
    [3, 4, 5],
    [6, 7]
]

for row in cartesian_product(domain):
    print(row)
