# Data Structure Study Plan 1
# Day 4
# 566. Reshape the matrix (Easy)

from typing import List

# (new) My solution, brute force (Runtime 80 ms, 96.5%; Memory 15.1 MB, 19%)
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        # My solution, brute force
        m = len(mat)
        n = len(mat[0])
        temp = [] # to store flattened numbers from mat
        out = [] # to store the final output
        if m * n == r * c:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
            for i in range(m):
                for j in range(n):
                    temp.append(mat[i][j])
            loop = 0 # initiate the index to loop through flattened numbers
            for i in range(r):
                seq = [] # to store each row element
                for j in range(c):
                    seq.append(temp[loop])
                    loop += 1
                out.append(seq) # to append each row as a list to the output list
            return out
        else: return mat


# Discussion #2, my brute force approach rewritten (88 ms, 69%; 15 mb, 37%)
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:        
        matrix = []
        one_row = []
        for i in mat:
            for j in i:
                one_row.append(j)
        if r*c == len(one_row):
            for i in range(0, len(one_row), c):
                matrix.append(one_row[i:i+c])
            return matrix
        else:
            return mat


# Discussion #1 by windycloud127 (88 ms, 69%; 14.8 mb, 74%)
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        A = [x for row in mat for x in row]
        if r * c == len(A):
            return [A[i * c: (i + 1) * c] for i in range(r)]
        else:
            return mat