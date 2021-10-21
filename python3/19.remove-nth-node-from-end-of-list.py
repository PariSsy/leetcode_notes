# Algorithm Study Plan
# Day 5
# 19. Remove Nth node from end of list

# Solutions 1 - 2: https://leetcode.com/problems/remove-nth-node-from-end-of-list/discuss/1164537/Short-and-Simple-One-Pass-Solution-w-Explanation-or-Beats-100-or-No-dummy-node-required!
# Solution 3: https://leetcode.com/problems/remove-nth-node-from-end-of-list/discuss/8802/3-short-Python-solutions

# Solution 1 - one-pointer, two-pass (32 ms, 83%)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        ptr, length = head, 0
        while ptr:
            ptr, length = ptr.next, length + 1
        if length == n:
            return ptr.next
        ptr = head
        for i in range(1, length - n):
            ptr = ptr.next
        ptr.next = ptr.next.next
        return head
## Time complexity = O(N), where N is the number of nodes in the given list.
## Space complexity = O(1), since only constant space is used.

# Solution 2 - Two-pointer, one-pass (35 ms, 64%)
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = slow = head
        for i in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast, slow = fast.next, slow.next
        slow.next = slow.next.next
        return head
## Time complexity: O(N), where N is the number of nodes in the given list. Although the time
##  complexity is the same as above, we have reduced the constant factor in it to half.
## Space complexity: O(1) since only constant space is used.

# Solution 3 - value-shifting (57 ms, 14%)
## Instead of removing the nth node, this solution removes the nth value
## It recursively determin the indexes (counting from back),
##  then shofts the values for all indexes larger than n,
##  and then always drop the head.
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def index(node):
            if not node:
                return 0
            i = index(node.next) + 1
            if i > n:
                node.next.val = node.val
            return i
        index(head)
        return head.next