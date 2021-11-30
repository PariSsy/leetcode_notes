# Data Structure Study Plan 1
# Day 3
# 350. Intersection of two arrays 2 (Easy)
## Three additional python solutions:
## https://leetcode.com/problems/intersection-of-two-arrays-ii/discuss/82247/Three-Python-Solutions

# My brute force solution (Runtime 64 ms, 40%; Memory 14.1 MB, 98%)
from typing import Collection, List
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        out = []
        if len(nums1) <= len(nums2):
            for num in nums1:
                if num in nums2:
                    out.append(num)
                    nums2.remove(num)
        else:
            for num in nums2:
                if num in nums1:
                    out.append(num)
                    nums1.remove(num)
        return out
## Time = O(m+n)
## Space = O(max(m,n))
## Based on Solution, this approach is similar to Hash Map,
##  but without the count, it uses more space, whereas Hash Map
##  has space complexity of O(min(n,m))

# Solution 2, two pointers (Runtime 48 ms, 76%; Memory 14.4 MB, 42%)
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1, nums2 = sorted(nums1), sorted(nums2)
        pt1 = pt2 = 0
        res = []        
        while True:
            try:
                if nums1[pt1] > nums2[pt2]:
                    pt2 += 1
                elif nums1[pt1] < nums2[pt2]:
                    pt1 += 1
                else:
                    res.append(nums1[pt1])
                    pt1 += 1
                    pt2 += 1
            except IndexError:
                break
        return res

# Solution 3, use dictionary to count (Runtime 40 ms, 97%; Memory 14.3 MB, 71%)
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts = {}
        res = []
        for num in nums1:
            # get() is a dictionary function that returns the value of a specific key
            counts[num] = counts.get(num, 0) + 1
        for num in nums2:
            if num in counts and counts[num] > 0:
                res.append(num)
                counts[num] -= 1
        return res

# Solution 4, use Counter(Runtime: 48 ms, 77%; Memory: 14.2 MB, 90%)
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts = Collection.Counter(nums1)
        res = []
        for num in nums2:
            if counts[num] > 0:
                res += num,
                counts[num] -= 1
        return res