# Algorithm 1 Study Plan
# Day 1
# 704. Binary Search

# Solution 1 (Runtime = 376 ms)
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        return -1
        
# Solution 2 (Runtime = 292 ms)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = bisect.bisect_left(nums, target)
        return index if index < len(nums) and nums[index] == target else -1