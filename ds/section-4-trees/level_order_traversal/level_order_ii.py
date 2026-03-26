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
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        q = deque([root])

        while q:
            level = []
    
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(level)

        return res[::-1]

root = [3,9,20,None,None,15,7]
print(Solution().levelOrderBottom(build_tree(root)))