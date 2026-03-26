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
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None or headB is None:
            return None
        
        p = headA
        q = headB

        while p != q:
            if p:
                p = p.next
            else:
                p = headB
            
            if q:
                q = q.next
            else:
                q = headA
        
        return p


common = build_list([8,4,5])

headA = build_list([4,1])
tailA = headA
while tailA.next:
    tailA = tailA.next
tailA.next = common

headB = build_list([5,6,1])
tailB = headB
while tailB.next:
    tailB = tailB.next
tailB.next = common

print_list(Solution().getIntersectionNode(headA, headB))