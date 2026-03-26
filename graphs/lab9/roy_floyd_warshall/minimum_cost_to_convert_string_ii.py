class Trie:
    def __init__(self):
        self.nxt = {}
        self.id = -1

    def insert(self, s, idx):
        node = self
        for c in s:
            if c not in node.nxt:
                node.nxt[c] = Trie()
            node = node.nxt[c]
        node.id = idx

    def match(self, s, start):
        node = self
        res = []
        for i in range(start, len(s)):
            c = s[i]
            if c not in node.nxt:
                break
            node = node.nxt[c]
            if node.id != -1:
                res.append((i, node.id))
        return res


class Solution:
    def minimumCost(self, source, target, original, changed, cost):
        n = len(source)

        # 1) map substring -> id
        mp = {}
        idx = 0

        def get_id(s):
            nonlocal idx
            if s not in mp:
                mp[s] = idx
                idx += 1
            return mp[s]

        m = len(original)
        orig_id = [get_id(original[i]) for i in range(m)]
        chg_id  = [get_id(changed[i])  for i in range(m)]

        # 2) dist matrix
        INF = 10**18
        dist = [[INF]*idx for _ in range(idx)]
        for i in range(idx):
            dist[i][i] = 0

        for o, c, w in zip(orig_id, chg_id, cost):
            dist[o][c] = min(dist[o][c], w)

        # 3) Floyd–Warshall
        for k in range(idx):
            for i in range(idx):
                if dist[i][k] == INF:
                    continue
                for j in range(idx):
                    if dist[k][j] == INF:
                        continue
                    nd = dist[i][k] + dist[k][j]
                    if nd < dist[i][j]:
                        dist[i][j] = nd

        # 4) build tries
        T1 = Trie()
        T2 = Trie()
        for i in range(m):
            T1.insert(original[i], orig_id[i])
            T2.insert(changed[i],  chg_id[i])

        # 5) DP
        dp = [INF]*(n+1)
        dp[0] = 0

        for i in range(n):
            # no change
            if source[i] == target[i]:
                dp[i+1] = min(dp[i+1], dp[i])

            # try substring transforms
            matches1 = T1.match(source, i)
            matches2 = T2.match(target, i)

            # map end -> list of ids
            end_to_ids1 = {}
            for end, id1 in matches1:
                end_to_ids1.setdefault(end, []).append(id1)

            end_to_ids2 = {}
            for end, id2 in matches2:
                end_to_ids2.setdefault(end, []).append(id2)

            # same end index
            for end in end_to_ids1:
                if end in end_to_ids2:
                    for id1 in end_to_ids1[end]:
                        for id2 in end_to_ids2[end]:
                            if dist[id1][id2] < INF:
                                dp[end+1] = min(dp[end+1], dp[i] + dist[id1][id2])

        return dp[n] if dp[n] < INF else -1

source = "abcd"
target = "acbe"
original = ["a","b","c","c","e","d"]
changed = ["b","c","b","e","b","e"]
cost = [2,5,5,1,2,20]
print(Solution().minimumCost(source, target, original, changed, cost))