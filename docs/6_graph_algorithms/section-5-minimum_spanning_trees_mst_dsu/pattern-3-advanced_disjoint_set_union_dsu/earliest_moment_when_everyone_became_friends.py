
def solve(logs, n):
    logs.sort(key = lambda x : x[0])
    parent = [i for i in range(n)]
    cnt = n

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    for log, u, v in logs:
        ru = find(u)
        rv = find(v)
        if ru != rv:
            parent[ru] = rv
            cnt -= 1

            if cnt == 1:
                return log

    return -1

logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]]
N = 6
print(solve(logs, N))