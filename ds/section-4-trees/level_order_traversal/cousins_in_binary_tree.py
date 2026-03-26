from typing import List, Optional
from collections import deque, defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def build_tree(arr):
    if not arr or arr[0] is None:
        return None

    nodes = [TreeNode(val) if val is not None else None for val in arr]

    child_index = 1
    for i in range(len(arr)):
        if nodes[i] is not None:
            if child_index < len(arr):
                nodes[i].left = nodes[child_index]
            child_index += 1

            if child_index < len(arr):
                nodes[i].right = nodes[child_index]
            child_index += 1

    return nodes[0]

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        res = []
        q = deque([root])

        while q:
            level = set()
            for _ in range(len(q)):
                node = q.popleft()
                level.add(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

                if node.left and node.right:
                    if node.left.val == x and node.right.val == y:
                        return False
                    elif node.left.val == y and node.right.val == x:
                        return False
            if x in level and y in level:
                return True

        return False
root = [1,2,3,4]
x = 4
y = 3
print(Solution().isCousins(build_tree(root), x, y))