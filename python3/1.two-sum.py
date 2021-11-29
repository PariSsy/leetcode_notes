# Data Structure Study Plan 1
# Day 2
# 1. Two sum (Easy)
## The full tutorial on two sum problems and variations:
## https://leetcode.com/problems/two-sum/discuss/737092/Sum-MegaPost-Python3-Solution-with-a-detailed-explanation

# My solution, brute force (7444 ms, 5%)
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            num1 = nums[i]
            for j in range(len(nums)):
                num2 = nums[j]
                if num1 + num2 == target:
                    if i != j:
                        return [i, j]

# Approach 1, brute force rewritten (runtime 4108 ms, 20%; memory 14.8 mb, 92%)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]
## Time: O(n^2)
## Space: O(1)

# Approach 3, one-pass hash table, original (runtime 52 ms, 97%; memory 15.4 mb, 42%)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
## Time: O(n)
## Space: O(n)


# Solution 2, one-pass hash table with enumerate() (52 ms, 97.5%)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, value in enumerate(nums):
            remaining = target - value
            if remaining in seen:
                return [i, seen[remaining]]
            seen[value] = i