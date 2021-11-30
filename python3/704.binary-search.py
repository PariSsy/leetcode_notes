# Algorithm 1 Study Plan
# Day 1
# 704. Binary Search (Easy)

from typing import List

# (rev 1) my solution, binary search - 232 ms, 85%; 15.7 mb, 31%
## See solution 1 for another writing
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        out = -1
        left, right = 0, len(nums) - 1
        while left <= right:
            travel = left + (right - left) // 2
            if nums[travel] == target:
                return travel
            elif nums[travel] > target:
                right = travel - 1
            else:
                left = travel + 1
        return out

# Solution 1 (Runtime = 376 ms)
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
## Time = O(log N)
## Space = O(1)
        
# Solution 2 (Runtime = 292 ms)
import bisect
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = bisect.bisect_left(nums, target)
        return index if index < len(nums) and nums[index] == target else -1