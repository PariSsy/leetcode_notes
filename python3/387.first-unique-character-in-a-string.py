# Data Structure Study Plan 1
# Day 6
# 387. First unique character in a string (Easy)

# New, using dictionary (68 ms, 95%; 14.1 mb, 97%)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        raw = {}
        repeat = {}
        for i in range(len(s)):
            if s[i] not in repeat:
                if s[i] not in raw:
                    raw[s[i]] = i
                else:
                    raw.pop(s[i]) # OR del raw[s[i]]
                    repeat[s[i]] = 1
        if len(raw) > 0:
            return min(raw.values())
        else:
            return -1


# Solution, hash map (92 ms, 88%; 14.4 mb, 71%)
# build hash map: character and how often it happens
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)
        # find the index
        for idx, cha in enumerate(s):
            if count[cha] == 1:
                return idx
        return -1