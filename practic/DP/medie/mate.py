
def solve(n, s, ok):
    up = [1] * n
    down = [1] * n
    pup = [-1] * n
    pdown = [-1] * n
    for i in range(n):
        for j in range(i):
            if s[j] < s[i]:
                if up[i] < down[j] + 1:
                    up[i] = down[j] + 1
                    pup[i] = j
            elif s[j] > s[i]:
                if down[i] < up[i] + 1:
                    down[i] = up[i] + 1
                    pdown[i] = j
    sol = max(max(up), max(down))
    print(sol)

    if ok == 1:
        best_up = max(range(n), key = lambda i : up[i])
        best_down = max(range(n), key = lambda i: down[i])

        if up[best_up] > down[best_down]:
            length = up[best_up]
            i = best_up
            mode = "up"
        else:
            length = down[best_down]
            i = best_down
            mode = "down"
        
        res = []
        while i != -1:
            res.append(s[i])
            if mode == "up":
                i = pup[i]
                mode = "down"
            else:
                i = pdown[i]
                mode = "up"
        res.reverse()
        print("".join(res))


s = input().strip()
ok = int(input())
solve(len(s), s, ok)