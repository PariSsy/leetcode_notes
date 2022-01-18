# Explore - Intro to Data Structure
# Arrays 101 - Intro
# Searching for items in an array
# 941. Valid mountain array (Easy)

# Solution discussion by calvinchankf, 2 pointers (264 ms, 29%)
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        left = 0
        for i in range(len(arr)-1):
            if arr[i+1] <= arr[i]:
                left = i
                break
        right = 0
        for i in range(len(arr)-1, 0, -1):
            if arr[i-1] <= arr[i]:
                right = i
                break
        if left == right and left > 0 and right+1 < len(arr):
            return True
        return False


# Solution, one pass (472 ms, 5%)
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        N = len(arr)
        i = 0
        
        # wall up
        while i+1 < N and arr[i] < arr[i+1]:
            i += 1
            
        # peak can't be first or last
        if i == 0 or i == N-1:
            return False
        
        # walk down
        while i+1 < N and arr[i] > arr[i+1]:
            i += 1
        
        return i == N-1


# new, brute force (321 ms, 17%)
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        # corner case fails when length of arr < 3
        if len(arr) < 3:
            return False
        peak, mover = max(arr), 0
        peak_index = arr.index(peak)
        # corner case if the peak is at the front or end
        if arr[0] == peak or arr[-1] == peak:
            return False
        # first check the left to peak
        while mover < peak_index:
            if arr[mover] >= arr[mover+1]:
                return False
            mover += 1
        # jump to the right of peak
        mover += 1
        # then check the right to peak
        while mover < len(arr):
            if arr[mover] >= arr[mover-1]:
                return False
            mover += 1
        # if all cases pass
        return True