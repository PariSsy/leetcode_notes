# Data Structure Study Plan 1
# Day 2
# 88. Merge sorted array (easy)

# (new) My solution (32 ms, 92%)
# with help from the discussion to handle m = 0 or n = 0 case
from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums2[n-1] > nums1[m-1]:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
            else:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
        # From discussion
        nums1[:n] = nums2[:n]

# Approach 1: merge and sort (runtime 36 ms, 76%; 14.1 mb, 87%)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """        
        for i in range(n):
            nums1[i + m] = nums2[i]
        nums1.sort()
## Time = O((n+m)log(n+m))
## Space = O(n)


# Approach 2: two-pointers, start from the beginning (runtime 36 ms, 76%; memory 14.4 mb, 33%)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Make a copy of the first m elements of nums1
        nums1_copy = nums1[:m]
        
        # Read pointers for nums1Copy and nums2 respectively
        p1 = p2 = 0
        
        # Compare elements from nums1Copy and nums2 and write the smallest to nums1
        for p in range(n+m):
            # We also need to ensure that p1 and p2 aren't over the boundaries
            # of their respective arrays
            if p2 >= n or (p1 < m and nums1_copy[p1] <= nums2[p2]):
                nums1[p] = nums1_copy[p1]
                p1 += 1
            else:
                nums1[p] = nums2[p2]
                p2 += 1
## Time = O(n+m)
## Space = O(m)


# Approach 3: two-pointers, start from the end (runtime 32 ms, 91%; memory 14.4 mb, 33%)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """        
        # Medium level solution
        # Set p1 and p2 to point to the end of their respective arrays
        p1 = m - 1
        p2 = n - 1
        
        # And move p backwards through the array, each time writing
        # the smallest value pointed at by p1 or p2
        for p in range(n + m - 1, -1, -1):
            if p2 < 0:
                break
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
## Time = O(n+m)
## Space = O(1)


# Discussion 1: two-pointers optimally written
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        a, b, write = m-1, n-1, m+n-1
        
        while b >= 0:
            if a >= 0 and nums1[a] > nums2[b]:
                nums1[write] = nums1[a]
                a -= 1
            else:
                nums1[write] = nums2[b]
                b -= 1            
            write -= 1