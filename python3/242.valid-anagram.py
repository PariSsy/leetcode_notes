# Data Structure Study Plan I
# Day 6
# 242. Valid anagram (Easy)

# (new) sorting (52 ms, 57%; 15.1 mb, 10%)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        s = sorted(s)
        t = sorted(t)
        for i in range(len(s)):
            if s[i] != t[i]:
                return False
        return True
## Time = O(n log n)
## Space = O(1)