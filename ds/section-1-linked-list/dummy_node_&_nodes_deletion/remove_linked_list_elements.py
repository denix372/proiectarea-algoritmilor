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
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        curr = head
        
        while curr and curr.next:
            # If current value equals the next value, skip the next node
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                # Otherwise, just move forward
                curr = curr.next
                
        return head

head = [1,2,6,3,4,5,6]
val = 6
print_list(Solution().removeElements(build_list(head), val))