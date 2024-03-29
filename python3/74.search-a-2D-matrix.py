# Data Structure Study Plan 1
# Day 5
# 74. Search a 2D matrix (Medium)

from typing import List

# Solution, binary search, optimal (Runtime 32 ms, 99.31%; Memory 14.9 MB, 34%)
## A sorted matrix m x n = a sorted array of length m x n
## row = idx // n
## col = idx % n
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        left, right = 0, m*n-1
        while left <= right:
            pivot_idx = (left + right) // 2
            pivot_element = matrix[pivot_idx // n][pivot_idx % n]
            if target == pivot_element:
                return True
            else:
                if target < pivot_element:
                    right = pivot_idx - 1
                else:
                    left = pivot_idx + 1
        return False