# Algorithm Study Plan
# Day 5
# 876. Middle of the Linked List

# Approach 1, output to array (32 ms, 71%)
# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        array = [head]
        while array[-1].next:
            array.append(array[-1].next)
        return array[len(array) // 2]
## Complexity analysis:
## Time complexity = O(N)
## Space complexity = O(N)

# Approach 2, fast and slow pointer (32 ms, 71%)
## When traversing the list with a pointer slow,
## make another pointer fast that traverses twice as fast.
## When fast reaches the end of the list, slow must be in the middle.

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Approach 2, fast and slow pointer
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
## Complexity analysis:
## Time complexity = O(N)
## Space complexity = O(1)