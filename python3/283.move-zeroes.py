# Algorithm Study Plan I
# Day 3
# 283. Move zeroes


 # (rev 2) two pointers (254 ms, 37%)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        curr = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            while nums[curr] != 0 and curr < i:
                curr += 1
            nums[curr], nums[i] = nums[i], nums[curr]


# (rev 1) two pointers (160 ms, 93%; 15.5 mb, 32%)
# See solution 2 for a better writing
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        anchor = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[anchor] = nums[i]
                anchor += 1
        nums[anchor:] = [0] * (len(nums) - anchor)


# (new) My solution using two pointers (reverse) (244 ms)
## reverse() function taken from 189
from typing import List

class Solution:
    def reverse(self, nums: list, start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end  - 1
            
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = m = 0
        a = [0] * n
        
        self.reverse(nums, 0, n - 1)
        
        while k < n:
            if nums[k] != 0:
                a[m] = nums[k]
                m += 1
            k += 1
            
        nums[:] = a
        self.reverse(nums, 0, m - 1)


# Solution 2 using two pointers, optimal coding writing (282 ms)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        anchor = 0
        for explorer in range(len(nums)):
            if nums[explorer] != 0:
                nums[anchor], nums[explorer] = nums[explorer], nums[anchor]
                anchor += 1

###########
# Explain #
###########

## nums = [0, 1, 0, 3, 12]
## anchor = 0
##
## when explorer = 0, anchor = 0
##  nums[explorer] = nums[0] = 0
##  -> next loop
##
## when explorer = 1, anchor = 0
##  nums[explorer] = nums[1] = 1 != 0
##  -> nums[anchor], nums[explorer] = nums[explorer], nums[anchor]
##  -> nums[0], nums[1] = nums[1], nums[0]
##  -> nums = [1, 0, 0, 3, 12]
##  -> anchor += 1 = 1
##
## when explorer = 2, anchor = 1
##  nums[explorer] = nums[2] = 0
##  -> next loop
##
## when explorer = 3, anchor = 1
##  nums[explorer] = nums[3] = 3 != 0
##  -> nums[1], nums[3] = nums[3], nums[1]
##  -> nums = [1, 3, 0, 0, 12]
##  -> anchor += 1 = 2
##
## when explorer = 4, anchor = 2
##  nums[explorer] = nums[4] = 12 != 0
##  -> nums[2], nums[4] = nums[4], nums[2]
##  -> nums = [1, 3, 12, 0, 0]
##  -> anchor += 1 = 3
##
## loop ends