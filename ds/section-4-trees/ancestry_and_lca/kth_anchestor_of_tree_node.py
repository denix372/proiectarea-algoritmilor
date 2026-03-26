from typing import List

class TreeAncestor:
    # binary lifting 
    def __init__(self, n: int, parent: List[int]):
        self.LOG = 17

        self.up = [[-1] * self.LOG for _ in range(n)]

        for i in range(n):
            self.up[i][0] = parent[i]
        
        for j in range(1, self.LOG):
            for i in range(n):
                if self.up[i][j - 1] != -1:
                    self.up[i][j] = self.up[self.up[i][j - 1]][j - 1]

    def getKthAncestor(self, node: int, k: int) -> int:
        for j in range(self.LOG):
            if k & (1 << j):
                node = self.up[node][j]
                if node == -1:
                    break
        return node


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)
treeAncestor = TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2])
print(treeAncestor.getKthAncestor(3, 1)) # returns 1 which is the parent of 3
print(treeAncestor.getKthAncestor(5, 2)) # returns 0 which is the grandparent of 5
print(treeAncestor.getKthAncestor(6, 3)) # returns -1 because there is no such ancestor