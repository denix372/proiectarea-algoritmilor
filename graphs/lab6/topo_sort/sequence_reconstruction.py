from collections import deque

def find_supersequence(nums, sequences):
    n = len(nums)
    graph = [[] for _ in range (n + 1)]
    indeg = [0] * (n + 1)
    for l in sequences:
        for i in range(len(l) - 1):
            graph[l[i]].append(l[i + 1])
            indeg[l[i + 1]] += 1
    q = deque()
    for i in range(1, n + 1):
        if indeg[i] == 0:
            q.append(i)
    order = []
    while q:
        if len(q) != 1:
            return False
        u = q.popleft()
        order.append(u)
        for v in graph[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    return order == nums

num = [4,1,5,2,6,3]
sequences =[[5,2,6,3],[4,1,5,2]]
print(find_supersequence(num, sequences))
