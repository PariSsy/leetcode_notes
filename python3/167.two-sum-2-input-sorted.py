# Algorithm Study Plan I
# Day 3
# 167. Two sum II - input array is sorted

# Solution 1 - two pointers (62 ms, 74%)
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        start, end = 0, len(nums) - 1
        while start < end:
            s = nums[start] + nums[end]
            if s == target:
                return [start + 1, end + 1]
            elif s > target:
                end -= 1
            else:
                start += 1

# Solution 2 - dictionary (60 ms, 89%)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # This method works because there's unique answer to each list
        # Which means for the two number that qualify, they're each unique 
        dic = {}
        for i, num in enumerate(nums):
            if target - num in dic:
                return [dic[target - num] + 1, i + 1]
            dic[num] = i

# Solution 3 - binary search (80 ms, 39%)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for index in range(len(numbers)):
            new_target = target - numbers[index]
            # Binary Search
            left, right = index + 1, len(numbers) - 1
            while left <= right:
                middle = (left + right) // 2
                if numbers[middle] < new_target:
                    left = middle + 1
                elif numbers[middle] > new_target:
                    right = middle - 1
                else:
                    return [index + 1, middle + 1]