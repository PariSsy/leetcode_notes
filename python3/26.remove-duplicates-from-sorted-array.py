# Explore - Intro to Data Structure
# Arrays 101
# 28. Remove duplicates from sorted array (Easy)

# solution discussion by zhengzhicong (88 ms, 70%)
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