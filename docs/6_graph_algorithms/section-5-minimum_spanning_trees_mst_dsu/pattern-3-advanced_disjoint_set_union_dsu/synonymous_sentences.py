from collections import defaultdict

class Solution:
    def generate_sentences(self, synonyms: list[list[str]], text: str) -> list[str]:
        parent = {}
        
        # --- 1: UNION FIND ---
        def find(x):
            if x not in parent:
                parent[x] = x
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
            
        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                parent[root_x] = root_y
                
        for u, v in synonyms:
            union(u, v)
            
        groups = defaultdict(list)
        for word in parent.keys():
            root = find(word)
            groups[root].append(word)
            
        for root in groups:
            groups[root].sort()
            
        # --- 2: BACKTRACKING ---
        words = text.split()
        res = []
        
        def back(i, sol):
            if i == len(words):
                res.append(" ".join(sol))
                return
                
            if words[i] in parent:
                root = find(words[i])
                for synonym in groups[root]:
                    sol.append(synonym)
                    back(i + 1, sol)
                    sol.pop()
            else:
                sol.append(words[i])
                back(i + 1, sol)
                sol.pop()

        back(0, [])
        return res

synonyms = [["happy","joy"],["sad","sorrow"],["joy","cheerful"]]
text = "I am happy today but was sad yesterday"
for x in (Solution().generateSentences(synonyms, text)):
    print(x)