# Data Structure Study Plan I
# Day 7
# 21. Merge two sorted lists (Easy)

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Solution 2, iteration (34 ms, 80%; 14.3 mb, 63%)
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # maintain an unchanging reference to node ahead of the return node
        prehead = ListNode(-1)
        
        prev = prehead
        while list1 and list2:
            if list1.val <= list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            prev = prev.next
## Time = O(n+m)
## Space = O(1)


# Solution 1, recursion (41 ms, 29%; 14.4 mb, 33%)
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        elif list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
## Time = O(n+m)
## Space = O(n+m)