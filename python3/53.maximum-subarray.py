# Data Structure Study Plan I
# Day 1
# 53. Maximum subarray (Easy)

# Solution 1 (Approach 2 from Solution) - Dynamic programming, Kadane's algorithm (740 ms, 56%)
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

# Solution 2 (Approach 3 from Solution) - Divide and conquer, advanced
# Runtime 2408 ms, 5%; Memory 27.7 MB, 98.5%
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Define a helper function
        def findBestSubarray(nums, left, right):
            # Base case - empty array
            if left > right:
                return -math.inf
            
            mid = (left + right) // 2
            curr = best_left_sum = best_right_sum = 0
            
            # Iterate from the middle to the beginning
            for i in range(mid - 1, left - 1, -1):
                curr += nums[i]
                best_left_sum = max(best_left_sum, curr)
            
            # Reset curr and iterate from the middle to the end
            curr = 0
            for i in range(mid + 1, right + 1):
                curr += nums[i]
                best_right_sum = max(best_right_sum, curr)
            
            # The best combined sum uses the middle element and
            # the best possible sum from each half
            best_combined_sum = nums[mid] + best_left_sum + best_right_sum
            
            # Find the best subarray possible from both halves
            left_half = findBestSubarray(nums, left, mid - 1)
            right_half = findBestSubarray(nums, mid + 1, right)
            
            # The largest of the 3 is the answer for any given input array
            return max(best_combined_sum, left_half, right_half)
        
        return findBestSubarray(nums, 0, len(nums) - 1)
## Time O(N logN)
## Space O(logN)