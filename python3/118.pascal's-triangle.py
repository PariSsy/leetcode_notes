# Data Structure Study Plan 1
# Day 4
# 118. Pascal's triangle (Easy)

from typing import List

# (rev 1) (24 ms, 97%; 14.2 mb, 83%)
class Solution:
    def generate(self, n: int) -> List[List[int]]:
        # (rev 1)
        out = [[1]] # Initiate the first row
        num = 1 # Initiate index for the second rwo
        while num < n:
            prev = out[num - 1] # Retrieve previous row
            new_middle = [] # Create empty array to hold values for the new row
            for i in range(len(prev) - 1): # Loop through the 1st to the 2nd last index of the previous row
                new_middle.append(prev[i] + prev[i+1]) # Add sum to the middle of the new row
            new = [1] + new_middle + [1] # Add boundaries to the new row
            out.append(new) # Append new row to final output
            num += 1 # Go to next row
        return out


# (new) My brute force solution (Runtime 28 ms, 88%; Memory 14.1 MB, 94%)
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # My brute force solution
        out = [[1]] # Initiate the initial list
        for i in range(1, numRows): # Loop through each row            
            seq = [0] * (i+1) # Initiate the list for row i            
            seq[0] = seq[i] = 1 # Initiate the head and tail entries           
            for j in range(1,i): # Calculate the sum of two numbers
                seq[j] = out[i-1][j-1] + out[i-1][j]
            out.append(seq)
        return out

# (new) my brute force improved (24 ms, 97%; 14 mb, 99.4%) 
class Solution:
    def generate(self, n: int) -> List[List[int]]:       
        out = [[1]] # Initiate the initial list
        for i in range(1, n): # Loop through each row            
            seq = [1] * (i+1) # Initiate the list for row i           
            for j in range(1,i): 
                seq[j] = out[i-1][j-1] + out[i-1][j] # Calculate the sum of two numbers
            out.append(seq)
        return out


# Solution 2, optimal - Dynamic programming, iterative (Runtime 20 ms, 99.5%; Memory 14.2 MB, 82%)
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = [[1]*i for i in range(1, numRows+1)] # Initialize triangle with all 1s
        for i in range(1, numRows):
            for j in range(1, i):
                pascal[i][j] = pascal[i-1][j] + pascal[i-1][j-1]
        return pascal
## Time = O(n^2)
## Space = O(n^2)


# Solution 3 - top down recursive (Runtime 32 ms, 71%; Memory 14.3 MB, 24%)
class Solution:
    def generate(self, n: int) -> List[List[int]]:
        def helper(n):
            if n:
                helper(n-1)             # generate above row first
                pascal.append([1]*n)    # insert current row into triangle
                for i in range(1, n-1): # update current row values using above row
                    pascal[n-1][i] = pascal[n-2][i] + pascal[n-2][i-1]
        pascal = []
        helper(n)
        return pascal