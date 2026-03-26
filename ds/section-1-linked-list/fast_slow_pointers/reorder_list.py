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
    def reverseList(self, head):
        prev, curr = None, head
        while curr:
            aux = curr.next
            curr.next = prev
            prev = curr
            curr = aux
        return prev
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        rev = self.reverseList(slow.next)
        slow.next = None

        # merge
        dummy = ListNode(0, head)
        curr = head
        while curr and rev:
            aux1 = curr.next
            aux2 = rev.next

            curr.next = rev
            rev.next = aux1
    
            curr = aux1
            rev = aux2
        
        return dummy.next
            
head = [1,2,3,4]
print_list(Solution().reorderList(build_list(head)))