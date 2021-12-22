# Explore - Intro to Data Structure
# Arrays 101 - Intro
# 1295. Find numbers with even number of digits (Easy)
## Test cases failed initially
[12,345,2,6,7896]
[555,901,482,1771]
[773,165,42,381,123]
[100000]


from typing import List

# (new) 44 ms, 98%; 14.4%
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        # Initiate number of elements with even number of digits
        numEven = 0
        # Loop through all numbers
        for num in nums:
            # Initiate division
            div = num // 10
            # Initiate number of digits
            ## When number < 100, digit is div + 1
            if div == 0:
                digit = 1
            ## When number >= 100, initiate digit = 2
            else:
                digit = 2
            # Divide the remaining division by 10 recursively
            while div >= 10:
                digit += 1
                div = div // 10
            # Check the digit of this number
            if digit % 2 == 0:
                numEven += 1
        # Return after all numbers were checked
        return numEven