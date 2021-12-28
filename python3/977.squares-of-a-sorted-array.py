# Algorithm Study Plan I
# Day 2
# 977. Squares of a sorted array

# (rev 2) two pointers (232 ms, 59%; 16.2 mb, 31%)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = [0] * n
        left, right = 0, n-1
        while left <= right:
            sq_left = nums[left] * nums[left]
            sq_right = nums[right] * nums[right]
            if sq_left <= sq_right:
                out[right - left] = sq_right
                right -= 1
            else:
                out[right - left] = sq_left
                left += 1
        return out

# Solution 1 - built-in function (300 ms)
from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(x*x for x in nums)

# Solution 2 - two pointers (260 ms)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        left = 0
        right = n - 1
        for i in range(n-1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                square = nums[right]
                right -= 1
            else:
                square = nums[left]
                left += 1
            result[i] = square * square
        return result