from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def build_tree(arr):
    if not arr or arr[0] is None:
        return None

    nodes = [TreeNode(val) if val is not None else None for val in arr]

    i = 0
    child = 1
    while child < len(arr):
        if nodes[i] is not None:
            if child < len(arr):
                nodes[i].left = nodes[child]
            child += 1

            if child < len(arr):
                nodes[i].right = nodes[child]
            child += 1
        i += 1

    return nodes[0]

def print_tree(root):
    if not root:
        print("[]")
        return

    res = []
    q = deque([root])

    while q:
        node = q.popleft()
        if node:
            res.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            res.append(None)

    while res and res[-1] is None:
        res.pop()

    print(res)


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def solve(node):
            if not node:
                return None

            tail_left = solve(node.left)
            tail_right = solve(node.right)
    
            if node.left:
                tail_left.right = node.right
                node.right = node.left
                node.left = None

            return tail_right or tail_left or node

        solve(root)

root = [1,2,5,3,4,None,6]
tree_root = build_tree(root)
Solution().flatten(tree_root)
print_tree(tree_root)