# Algorithm Study Plan I
# Day 6
# 3. Longest substring without repeating characters


# Solution discussion 1 by kxguoniu
# 56 ms, 85%; 14.3 mb, 81%
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dicts = {}
        maxlength = start = 0
        for i, value in enumerate(s):
            if value in dicts:
                sums = dicts[value] + 1
                if sums > start:
                    start = sums
            num = i - start + 1
            maxlength = max(maxlength, num)
            dicts[value] = i
        return maxlength


# Solution discussion 1 improgement by user2369Q
# 32 ms, 100%; 14.5 mb, 7%
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_len, start, chars = 0, -1, {}
        for i, v in enumerate(s):
            if v in chars and chars[v] > start:
                start = chars[v]
            elif i - start > longest_len:
                longest_len = i - start
            chars[v] = i
        return longest_len



# (rev 1) brute force (1068 ms, 5%; 14.3 mb, 81%)
## Pay attention to test case ["", " "]
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p1 = p2 = 0
        n = len(s)
        store = dict()
        out = 0
        while p1 <= n-1 and p2<= n-1:
            if s[p2] not in store:
                store[s[p2]] = p2 - p1
                p2 += 1
                out = max(out, p2 - p1)
            else:
                out = max(out, p2 - p1)
                p1 += store[s[p2]] + 1
                p2 = p1
                store = dict()
        return out


# Solution 3, Sliding window optimized - using HashMap (71 ms, 52%; 14.3 mb, 56%)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        # mp stores the current index of a character
        mp = {}
        i = 0
        # try to extend the range [i,j]
        for j in range(n):
            if s[j] in mp:
                i = max(mp[s[j]], i)
            ans = max(ans, j - i + 1)
            mp[s[j]] = j + 1
        return ans
## Time = O(2n) = O(n)
## Space = O(min(n,m))


# Solution 2, sliding window (64 ms, 70%; 14.5 mb, 7%)
## If a substring Sij from index i to j-1 is already checked to have no duplicates,
##  we only need to check if s[j] is already in the substring Sij.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = [0] * 128
        left = right = 0
        res = 0
        while right < len(s):
            r = s[right]
            # ord() function returns an integer representing the Unicode character.
            chars[ord(r)] += 1
            while chars[ord(r)] > 1:
                l = s[left]
                chars[ord(l)] -= 1
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res
## Time = O(2n) = O(n)
## Space = O(min(n,m))


# Solution 1, brute force
## Time limit exceeded
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def check(start, end):
            chars = [0] * 128
            for i in range(start, end + 1):
                c = s[i]
                chars[ord(c)] += 1
                if chars[ord(c)] > 1:
                    return False
            return True
        n = len(s)
        res = 0
        for i in range(n):
            for j in range(i,n):
                if check(i, j):
                    res = max(res, j - i + 1)
        return res
## Time = O(n^3)
## Space = O(min(n,m)) - we need O(k) space for checking a substring has no duplicates,
### where k is the size of the Set.