# Explore - Intro to Data Structure
# Arrays 101
# 26. Remove duplicates from sorted array (Easy)


# rev 1, two pointers (163 ms, 19%)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        keeper = mover = 0
        while mover < len(nums):
            if nums[keeper] < nums[mover]:
                keeper += 1
                nums[keeper] = nums[mover]
            else:
                mover += 1              
        return keeper+1


# solution discussion by zhengzhicong, one pointer (88 ms, 70%)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        mover = 1
        if len(nums) == 0:
            return 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[mover] = nums[i]
                mover += 1
        return mover