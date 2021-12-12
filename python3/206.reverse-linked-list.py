# Data Structure Study Plan I
# Day 8
# 206. Reverse linked list (Easy)


from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Discussion 3 (by MaksymSkorupskyi) (52 ms, 17%; 15.6 mb, 77%)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = None
        curr_node = head
        while curr_node:
            next_node = curr_node.next # Remember next node
            curr_node.next = prev_node # REVERSE
            prev_node = curr_node # Used in the next iteration
            curr_node = next_node # Move to next node
        head = prev_node
        return head


# Discussion 2 (by moby), recursive (41 ms, 27%; 19.1 mb, 7%)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:       
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p


# Discussion 1 (by moby), iterative (45 ms, 23%; 15.7 mb, 46%)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev
## Time = O(N)
## Space = O(1)