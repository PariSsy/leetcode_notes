# Algorithm Study Plan I
# Day 1
# 35. Search insert position

# Solution 1 (48 ms, 80%)
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            m = left + (right - left) // 2
            if nums[m] == target:
                return m
            if nums[m] < target:
                left = m + 1
            else:
                right = m - 1
        return left