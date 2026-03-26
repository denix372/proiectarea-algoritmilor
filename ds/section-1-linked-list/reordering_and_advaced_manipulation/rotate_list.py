from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_list(arr):
    dummy = ListNode()
    tail = dummy
    for x in arr:
        tail.next = ListNode(x)
        tail = tail.next
    return dummy.next

def print_list(node):
    vals = []
    while node:
        vals.append(node.val)
        node = node.next
    print(vals)

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        curr = head
        n = 1
        while curr.next:
            curr = curr.next
            n += 1
        
        rot = k % n
        if rot == 0:
            return head

        curr.next = head
        for _ in range(n - rot):
            curr = curr.next
        
        aux = curr.next
        curr.next = None
        return aux

head = [1,2,3,4,5]
k = 2
print_list(Solution().rotateRight(build_list(head), k))