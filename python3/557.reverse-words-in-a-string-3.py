# Algorithm Study Plan
# Day 4
# 557. Reverse words in a string III

# Approach 1, Two pointer solution (215 ms, 5%; 14.9 mb, 28%)
class Solution:
    def reverseWords(self, s: str) -> str:
        """Two-pointers implementation, reverse each word within string"""
        l = 0  # start of current word
        r = 0  # position after end of current word
        #   For each word in the string
        while r < len(s):
            #   Advance r to end-of-current-word or end-of-string
            while r < len(s) and s[r] != ' ':
                r += 1
            #   reverse current word within s and assign result back to s
            s = s[:l] + s[l:r][::-1] + s[r:]
            #   Advance l and r to the start of next word
            r += 1
            l = r
        return s

# Approach 2, Python built-in function (81 ms, 23%; 14.7, 76%)
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        for i in range(len(s)):
            s[i] = s[i][::-1]
        return " ".join(s)