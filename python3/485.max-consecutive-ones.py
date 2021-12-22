# Explore - Intro to Data Structure
# Arrays 101 - Intro
# 485. Max Consecutive Ones (Easy)

from typing import List

# Solution 2, one-liner by Stefan Pochmann
# 348 ms, 76%; 15.2 mb, 6%
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ## Convert the list into a string using map and join
        ## Splits the string on 0
        return max(map(len, ''.join(map(str, nums)).split('0')))


# Solution 1 (348 ms, 76%; 14.5 mb, 17%)
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOne = curOne = 0
        for i in nums:
            if i == 1:
                curOne += 1
            else:
                maxOne = max(curOne, maxOne)
                curOne = 0
        return max(curOne, maxOne)
## Time = O(N)
## Space = O(1)


# (new) (360 ms; 14.3 mb)
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOne = curOne = 0
        for i in nums:
            if i == 1:
                curOne += 1
                maxOne = max(curOne, maxOne)
            else:
                curOne = 0
        return maxOne