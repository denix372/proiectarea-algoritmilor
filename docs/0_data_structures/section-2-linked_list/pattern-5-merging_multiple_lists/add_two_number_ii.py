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
    def add_two_numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1, s2 = [], []
        
        while l1:
            s1.append(l1.val)
            l1 = l1.next
            
        while l2:
            s2.append(l2.val)
            l2 = l2.next
            
        carry = 0
        head = None
        
        while s1 or s2 or carry:
            val1 = s1.pop() if s1 else 0
            val2 = s2.pop() if s2 else 0
            
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10
            
            newNode = ListNode(digit)
            newNode.next = head
            head = newNode
            
        return head

l1 = [7,2,4,3]
l2 = [5,6,4]
print_list(Solution().addTwoNumbers(build_list(l1), build_list(l2)))