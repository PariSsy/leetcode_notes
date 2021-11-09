# Data Structure Study Plan 1
# Day 5
# 36. Valid sudoku (Medium)
## Solutions:
## 1. https://leetcode.com/problems/valid-sudoku/discuss/15460/1-7-lines-Python-4-solutions
## 2. (optimal) https://leetcode.com/problems/valid-sudoku/discuss/729180/Python-solutions-or-Single-Traversal-or-Single-Dictionary
## 3. (My logic correct way) https://leetcode.com/problems/valid-sudoku/discuss/1414952/Python-Super-Easy-SET-Validation

import collections
from typing import Collection, List
# Solution 1, using Counter() - (Runtime 100 ms, 61%; Memory 14.4 MB, 15%)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:       
        # Solution 1, using Counter
        return 1 == max(Collection.Counter(
            x
            for i, row in enumerate(board)
            for j, c in enumerate(row)
            if c != '.'
            for x in ((c,i), (j,c), (i//3, j//3, c))
        ).values() or (1,)) # to handle empty board

# Solution 2, using len(set) - (Runtime 92 ms, 90%; Memory 14.3 MB, 42%)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = sum((
            [(c, i), (j, c), (i//3, j//3, c)]
            for i, row in enumerate(board)
            for j, c in enumerate(row)
            if c != '.'
        ), [])
        return len(seen) == len(set(seen))

# Solution 3, using any() - (Runtime 92 ms, 90%; Memory 14.2 MB, 70%)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        return not any(
            x in seen or seen.add(x)
            for i, row in enumerate(board)
            for j, c in enumerate(row)
            if c != '.'
            for x in ((c, i), (j, c), (i//3, j//3, c))
        )

# Solution 4, single traversal, optimal (Runtime 88 ms, 97%; Memory 14.4 MB 42%)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Solution 4, single traversal
        boardMap = collections.defaultdict(list)
        for x in range(9):
            for y in range(9):
                char = board[x][y]
                if char != '.':
                    if char in boardMap:
                        for pos in boardMap[char]:
                            if (pos[0]==x) or (pos[1]==y) or (pos[0]//3 == x//3 and pos[1]//3 == y//3):
                                return False
                    boardMap[char].append((x,y))
        return True

# Solution 5 (Runtime 100 ms, 61%; Memory 14.4, 42%)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def valid(li):
            if len(li) == len(set(li)):
                return True
            return False
        # row validations
        for i in range(9):
            li = [board[i][j] for j in range(9) if board[i][j] != '.']
            if not valid(li):
                return False
        # col validations
        for i in range(9):
            li = [board[j][i] for j in range(9) if board[j][i] != '.']
            if not valid(li):
                return False
        # block validations
        for i in range(0,9,3):
            for j in range(0,9,3):
                block = [board[k][l] for k in range(i,i+3) for l in range(j,j+3) if board[k][l] != '.']
                if not valid(block):
                    return False
        return True