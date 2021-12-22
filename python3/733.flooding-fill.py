# Algo Study Plan I
# Day 7 - DFS/BFS
# 733. Flooding fill (Easy)

from typing import List

# Solution 1, depth-first search
# 76 ms, 67%; 14.6 mb, 11%
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        R, C = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor: return image
        # create a function dfs() to floodfill a target pixel
        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r >= 1: dfs(r-1, c)
                if r+1 < R: dfs(r+1, c)
                if c >= 1: dfs(r, c-1)
                if c+1 < C: dfs(r, c+1)
        dfs(sr, sc)
        return image
## Time = O(N)
## Space = O(N)