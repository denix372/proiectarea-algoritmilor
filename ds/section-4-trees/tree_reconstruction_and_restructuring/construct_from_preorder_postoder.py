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
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        postorder_map = {val: idx for idx, val in enumerate(postorder)}

        i = 0
        def solve(left, right):
            nonlocal i
            if left > right:
                return None
            
            root_val = preorder[i]
            i += 1
            root = TreeNode(root_val)

            # this means the node is a leaf
            if left == right:
                return root
            
            
            left_root_val = preorder[i] # basically the previous preorder[i + 1]
            mid = postorder_map[left_root_val]
            # we include mid this time beacuse is root of thre subtree
            root.left = solve(left, mid)
            # exclude right because right is the root we already exatracted
            root.right = solve(mid + 1, right - 1)

            return root
        
        return solve(0, len(postorder) - 1)

preorder = [1,2,4,5,3,6,7]
postorder = [4,5,2,6,7,3,1]
print_tree(Solution().constructFromPrePost(preorder, postorder))