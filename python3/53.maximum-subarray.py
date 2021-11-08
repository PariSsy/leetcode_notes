# Data Structure Study Plan I
# Day 1
# 53. Maximum subarray (Easy)

# Solution 1 (740 ms, 56%)
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = maxSum = nums[0]
        for num in nums[1:]:
            curSum = max(curSum, 0) + num # Abandons previsou sequence and restart at num if curSum < 0
            maxSum = max(curSum, maxSum)
        return maxSum
## Time O(n)
## Space O(1)