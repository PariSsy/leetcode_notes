# Explore - Intro to Data Structure
## Arrays 101 - In-Place Operations
## 905. Sort array by parity (Easy)


# (new) two pointers (109 ms, 36%)
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        anchor = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[anchor], nums[i] = nums[i], nums[anchor]
                anchor += 1
        return nums