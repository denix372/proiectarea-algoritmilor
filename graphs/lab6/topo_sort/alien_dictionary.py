from collections import deque

def alien_dictionary(words):
    n = len(words)
    chars = set("".join(words))
    graph = {c : [] for c in chars}
    indeg = {c : 0 for c in chars}

    for i in range(n - 1):
        w1 = words[i]
        w2 = words[i + 1]

        if len(w1) > len(w2) and w1.startswith(w2):
            return ""
        for j in range(min(len(w1), len(w2))):
            if w1[j] != w2[j]:
                a, b = w1[j], w2[j]
                if b not in graph[a]:
                    graph[a].append(b)
                    indeg[b] += 1
                break
    q = deque()
    for c in sorted(chars):
        if indeg[c] == 0:
            q.append(c)
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for w in sorted(graph[u]):
            indeg[w] -= 1
            if indeg[w] == 0:
                q.append(w)
    print(order)
    if len(order) == len(chars):
        return "".join(order)
    return ""

words = ["wrt","wrf","er","ett"]
print(alien_dictionary(words)) 