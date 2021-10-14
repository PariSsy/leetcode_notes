# Algorithm Study Plan I
# Day 1
# 278. First bad version

# My solution (51 ms)

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        left, right = 1, n
        while left <= right:
            target = left + (right - left) // 2
            if isBadVersion(target):
                if isBadVersion(target - 1):
                    right = target - 1
                else:
                    return target
            else:
                left = target + 1

# Solution 2 (75 ms)
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left
        