
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
    def rob(self, root: TreeNode | None) -> int:
        
        def dfs(node):
            if not node:
                return (0, 0)
            
            lt, ls = dfs(node.left)
            rt, rs = dfs(node.right)

            take = node.val + ls + rs

            skip = max(lt, ls) + max(rt, rs) # max_left(take + skip) + max_right(take, skip)

            return (take, skip)
    
        return max(dfs(root))

root = [3,2,3,None,3,None,1]
print(Solution().rob(build_tree(root)))