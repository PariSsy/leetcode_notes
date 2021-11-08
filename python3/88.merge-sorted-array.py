# Data Structure Study Plan 1
# Day 2
# 88. Merge sorted array (easy)

# My solution (32 ms, 92%)
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