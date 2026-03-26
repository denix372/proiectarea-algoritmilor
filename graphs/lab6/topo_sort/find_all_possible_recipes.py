from collections import deque, defaultdict
from typing import List
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        indeg = defaultdict(int)

        for r, ing_list in zip(recipes, ingredients):
            indeg[r] = len(ing_list)
            for ing in ing_list:
                graph[ing].append(r)
        q = deque(supplies)
        res =[]

        while q:
            u = q.popleft()
            for v in graph[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    res.append(v)
                    q.append(v)
        return res
        
recipes = ["bread","sandwich","burger"]
ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]]
supplies = ["yeast","flour","meat"]
print(Solution().findAllRecipes(recipes, ingredients, supplies))