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
    def build_tree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        i = len(postorder) - 1
        def solve(left, right):
            nonlocal i
            if left > right:
                return None
            
            root_val = postorder[i]
            i -= 1
            root = TreeNode(root_val)

            mid = inorder_map[root_val]
            # postorder -> we build RIGHT first
            root.right = solve(mid + 1, right)
            root.left = solve(left, mid - 1)
           
            return root
        
        return solve(0, len(inorder) - 1)

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
print_tree(Solution().buildTree(inorder, postorder))