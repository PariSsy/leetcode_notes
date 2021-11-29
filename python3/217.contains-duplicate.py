# Data Structure Study Plan I
# Day 1
# 217. Contains duplicate (Easy)

# (New round) My solution 1, brute force (120 ms, 72%)
from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
            else:
                i += 1
        return False

# Solution 2 (108 ms, 98%)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Using set() to return distinct values
        if len(nums) == len(set(nums)):
            return False
        else:
            return True

# (Rev 1) My solution 1 (108 ms, 98%)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) > len(set(nums)):
            return True
        return False