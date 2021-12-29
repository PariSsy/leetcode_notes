# Explore - Intro to Data Structure
# Arrays 101
# 27. Remove element (Easy)

from typing import List

# Solution discussion by zhengzhicong (32 ms, 76%; 14 mb, 99%)
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1
        return count


# new, two pointers (51 ms, 8%; 14.2 mb, 72%)
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        travel = replace = 0
        while travel < len(nums):
            if nums[travel] == val:
                travel += 1
            else:
                nums[replace] = nums[travel]
                travel += 1
                replace += 1
        return replace