from typing import List
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            ra = find(a)
            rb = find(b)
            if ra == rb:
                return
            if rank[ra] > rank[rb]:
                parent[rb] = ra
            elif  rank[ra] < rank[rb]:
                parent[ra] = rb
            else:
                parent[ra] = rb
                rank[ra] += 1
        parent = {}
        rank = {}
        email = {}

        for acc in accounts:
            name = acc[0]
            for e in acc[1:]:
                if e not in parent:
                    parent[e] = e
                    rank[e] = 0
                    email[e] = name

        for acc in accounts:
            first = acc[1]
            for e in acc[2:]:
                union(first, e)
        
        groups = {}
        for e in parent:
            root = find(e)
            if root not in groups:
                groups[root] = []
            groups[root].append(e)
        res = []
        for root, emails in groups.items():
            name = email[root]
            res.append([name] + sorted(emails))
        return res

accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],
            ["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],
            ["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],
            ["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],
            ["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]

for a in Solution().accountsMerge(accounts):
    print(a)