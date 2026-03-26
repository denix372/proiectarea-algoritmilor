from collections import deque

class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def build_tree(arr):
    if not arr or arr[0] is None:
        return None

    nodes = [Node(val) if val is not None else None for val in arr]

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
    level = root

    while level:
        node = level
        next_level_start = None

        while node:
            res.append(node.val)

            if not next_level_start:
                if node.left:
                    next_level_start = node.left
                elif node.right:
                    next_level_start = node.right

            node = node.next

        res.append("#")
        level = next_level_start

    print(res)

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        node = root
        while node:
            dummy = Node(0)
            tail = dummy

            while node:
                if node.left:
                    tail.next = node.left
                    tail = tail.next
                if node.right:
                    tail.next = node.right
                    tail = tail.next
                
                node = node.next

            node = dummy.next
        
        return root

root = [1,2,3,4,5,None,7]
print_tree(Solution().connect(build_tree(root)))