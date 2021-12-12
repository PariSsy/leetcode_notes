# Data Structure Study Plan I
# Day 7
# 141. Linked list cycle (Easy)

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Solution 2, Floyd's cycle finding algorithm (82 ms, 17%; 17.7 mb, 56%)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
## Time = O(n)
## Space = O(1)


# Solution 1, hash table (65 ms, 28%; 18 mb, 17%)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodes_seen = set()
        while head is not None:
            if head in nodes_seen:
                return True
            nodes_seen.add(head)
            head = head.next
        return False
## Time = O(n)
## Space = O(n)