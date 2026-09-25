from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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
    def build_tree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: idx for idx, val in enumerate(inorder)}

        i = 0
        def solve(left, right):
            nonlocal i
            if left > right:
                return None
            
            root_val = preorder[i]
            i += 1
            root = TreeNode(root_val)

            mid = inorder_map[root_val]
            root.left = solve(left, mid - 1)
            root.right = solve(mid + 1, right)

            return root
        
        return solve(0, len(inorder) - 1)

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
print_tree(Solution().buildTree(preorder, inorder))