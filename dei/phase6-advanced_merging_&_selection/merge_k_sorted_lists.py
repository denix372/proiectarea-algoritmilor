from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val}"
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
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        return self.mergeRange(lists, 0, len(lists) - 1)

    def mergeRange(self, lists, left, right):
        if left == right:
            return lists[left]
        mid = (left + right) // 2
        l1 = self.mergeRange(lists, left, mid)
        l2 = self.mergeRange(lists, mid + 1, right)
        return self.mergeTwo(l1, l2)

    def mergeTwo(self, a, b):
        dummy = ListNode()
        tail = dummy
        while a and b:
            if a.val < b.val:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next
        tail.next = a or b
        return dummy.next
    

lists = [[1,4,5],[1,3,4],[2,6]]
lists = [build_list(l) for l in lists]


merged = Solution().mergeKLists(lists)
print_list(merged)
