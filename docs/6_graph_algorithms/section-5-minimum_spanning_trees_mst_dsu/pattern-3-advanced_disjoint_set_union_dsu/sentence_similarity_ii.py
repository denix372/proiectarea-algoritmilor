
def solve(sentence1, sentence2, similarPairs):
    if len(sentence1) != len(sentence2):
        return False

    parent = {}

    def find(x):
        if x not in parent:
            parent[x] = x

        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        rx = find(x)
        ry = find(y)
        if rx != ry:
            parent[rx] = ry

    for u, v in similarPairs:
        union(u, v)

    for w1, w2 in zip(sentence1, sentence2):
        if w1 == w2:
            continue

        if find(w1) != find(w2):
            return False
    return True


sentence1 = ["I", "am", "happy"]
sentence2 = ["I", "am", "joyful"]
similarPairs = [["happy", "joyful"]]
solve(sentence1, sentence2, similarPairs)