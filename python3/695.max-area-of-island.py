# Algo Study Plan I
# Day 7 BFS/DFS
# 695. Max area of island (Medium)

from typing import List

# Solution 1, depth-first search (recursive)
# 160 ms, 40%; 18.2 mb, 8%
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        def area(r, c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])
                   and (r,c) not in seen and grid[r][c]):
                return 0
            seen.add((r,c))
            return (1 + area(r+1, c) + area(r-1, c) +
                   area(r, c-1) + area(r, c+1))
        return max(area(r,c)
                  for r in range(len(grid))
                  for c in range(len(grid[0])))
## Time = O(R * C)
## Space = O(R * C)