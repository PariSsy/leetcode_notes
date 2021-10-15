# Algorithm Study Plan I
# Day 2
# 189. Rotate array

# My solution (time limit exceeded)
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        while k > 0:
            if len(nums[0:(n-1)]) == 1:
                nums[:] = [nums[n-1], nums[0]]
            else:
                nums[:] = [nums[n-1]] + nums[0:(n-1)]
            k -= 1

# Solution 1, brute force (time limit exceeded)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # speed up the rotation
        ## k may > n, thus:
        k %= len(nums) ## k = k % len(nums), remainder of x divided by y
        for i in range(k):
            previous = nums[-1]
            for j in range(len(nums)):
                nums[j], previous = previous, nums[j]

# Solution 2, using extra array (341 ms, 31%)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        a = [0] * n
        for i in range(n):
            a[(i + k) % n] = nums[i]
        nums[:] = a

###########
# Explain #
###########
n = 7
k = 3
a = [0] * n
print("n is", n, ", k is", k, ":")
for i in range(n):
    print("i is", i, ", (i + k) % n is", (i + k) % n)
##########
# Output #
##########
# n is 7 , k is 3 :
# i is 0 , (i + k) % n is 3
# i is 1 , (i + k) % n is 4
# i is 2 , (i + k) % n is 5
# i is 3 , (i + k) % n is 6
# i is 4 , (i + k) % n is 0
# i is 5 , (i + k) % n is 1
# i is 6 , (i + k) % n is 2

# Solution 3, using cyclic replacements (272 ms, 43%)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n        
        
        start = count = 0
        while count < n:
            current, prev = start, nums[start]
            while True:
                next_idx = (current + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                current = next_idx
                count += 1
                
                if start == current:
                    break
            start += 1

# Solution 4, using reverse (optimal, 212 ms, 87%)
class Solution:
    def reverse(self, nums: list, start: int, end:int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1
    
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        
        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)
###########
# Explain #
###########
# Let n = 7 and k = 3.
# Original List                   : 1 2 3 4 5 6 7
# After reversing all numbers     : 7 6 5 4 3 2 1
# After reversing first k numbers : 5 6 7 4 3 2 1
# After revering last n-k numbers : 5 6 7 1 2 3 4 --> Result