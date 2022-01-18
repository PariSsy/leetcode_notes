# Explore - Intro to Data Structure
# Arrays 101 - Intro
# In-place operations
# 1299. Replace elements with greatest element on right

# Discussion by Mrmagician (158 ms, 53%)
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        m = -1
        i = len(arr) - 1
        while i >= 0:
            temp = arr[i]
            arr[i] = m
            if temp > m:
                m = temp
            i -= 1
        return arr


# Discussion by baconbakenator, not in-place (112 ms, 98%)
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        out = [-1]
        greatest = 0
        # the ::-1 shifts all elements in arr to the left by 1
        for num in arr[::-1]:
            if greatest < num:
                greatest = num
            out.append(greatest)
        out.pop()
        return out[::-1]


# new #2, 2 pointers to optimize the middle part (221 ms, 37%)
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # reduce number of times the max is recalculated
        if len(arr) == 1:
            arr = [-1]
            return arr
        i, curr_max = 0, max(arr[1:])
        # left proceed until before the last element
        while i < len(arr) - 1:
            arr[i] = curr_max
            i += 1
            if arr[i] == curr_max and i+1 <= len(arr) - 1:
                curr_max = max(arr[i+1:])
        arr[-1] = -1
        return arr


# new #1, brute force (5336 ms, 8%)
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            arr = [-1]
            return arr
        for i in range(len(arr)-1):
            arr[i] = max(arr[i+1:])
        arr[-1] = -1
        return arr