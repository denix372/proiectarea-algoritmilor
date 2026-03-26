n = int(input())
res = []
def back(sol, i):
    if len(sol) == n:
        print("".join(sol))
        return
    if i == 0:
        back(sol + '1', 1)
        back(sol + '0', 0)
    else:
        back(sol + '0', 1)
        back(sol + '1', 0)
back('', 1)