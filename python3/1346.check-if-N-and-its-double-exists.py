# Explore - Intro to Data Structure
# Arrays 101
# 1346. Check if N and its double exists (Easy)


# HashSet by rock (80 ms, 28%)
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        for i in arr:
            if 2 * i in seen or i / 2 in seen:
                return True
            seen.add(i)
        return False