# Explore - Intro to Data Structure
# Arrays 101 - Intro
# 1089. Dupliate zeros (Easy)

from typing import List


# Solution - two pass, O(1) space (60 ms, 98%; 15 mb, 8%)
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        possible_dups = 0
        length = len(arr) - 1
        # Find the number of zeros to be duplicated
        for left in range(length+1):
            # stop when left points beyond the last element in the
            # original list which would be part of the modified list
            if left > length - possible_dups:
                break
            # Count the zeros
            if arr[left] == 0:
                # Edge case: this zero can't be duplicated. We have
                # no more space as left is pointing to the last
                # element which could be included
                if left == length - possible_dups:
                    arr[length] = 0 # for this zero we just copy it
                    length -= 1
                    break
                possible_dups += 1
        # Start backwards from the last element which would be part of
        # new list
        last = length - possible_dups
        # Copy zero twice, and non zero once
        for i in range(last, -1, -1):
            if arr[i] == 0:
                arr[i + possible_dups] = 0
                possible_dups -= 1
                arr[i + possible_dups] = 0
            else:
                arr[i + possible_dups] = arr[i]
## Runtime = O(N)
## Space = O(1)


# (new) 68 ms, 82%; 14.8 mb, 84%
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        dup = arr[:]
        j = 0 # initiate j to loop through duplicate
        i = 0 # initiate i to loop through arr
        while j < len(dup):
            # If the current num is not 0, then hold and proceed by 1
            if dup[j] != 0:
                arr[i] = dup[j]
                i += 1
            # Else the current num = 0, then duplicate and proceed by 2
            elif i+1 < len(arr):
                arr[i] = arr[i+1] = 0
                i += 2
                dup.pop(-1) # remove the last element from duplicate
            else:
                arr[i] = 0
                i += 2
                dup.pop(-1)
            j += 1