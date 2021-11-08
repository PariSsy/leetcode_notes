# Data Structure Study Plan 1
# Day 2
# 1. Two sum (Easy)
## The full tutorial on two sum problems and variations:
## https://leetcode.com/problems/two-sum/discuss/737092/Sum-MegaPost-Python3-Solution-with-a-detailed-explanation

# My solution, brute force (7444 ms, 5%)
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute force
        for i in range(len(nums)):
            num1 = nums[i]
            for j in range(len(nums)):
                num2 = nums[j]
                if num1 + num2 == target:
                    if i != j:
                        return [i, j]

# Solution 2, optimal (52 ms, 97.5%)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, value in enumerate(nums):
            remaining = target - value
            if remaining in seen:
                return [i, seen[remaining]]
            else:
                seen[value] = i