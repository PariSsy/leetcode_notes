# Algorithm Study Plan
# Day 4
# 344. Reverse string

# My solution - two pointers (267 ms, 29%)
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start, end = 0, len(s) - 1
        while start < end:
            head = s[start], tail = s[end]
            s[start], s[end] = tail, head
            start, end = start + 1, end - 1

# Python function
class Solution:
    def reverseString(self, s):
        s.reverse()

# Solutions
# Approach 1: Recursion, In-Place, O(N) Space
class Solution:
    def reverseString(self, s):
        def helper(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                helper(left + 1, right - 1)

        helper(0, len(s) - 1)
# Complexity analysis:
## Time complexity : O(N) time to perform N/2 swaps.
## Space complexity : O(N) to keep the recursion stack.

# Approach 2: Two Pointers, Iteration, O(1) Space
class Solution:
    def reverseString(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1
# Complexity analysis:
## Time complexity : O(N) time to perform N/2 swaps.
## Space complexity : O(1), it's a constant space solution.