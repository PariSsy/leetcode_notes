# Algorithm Study Plan 1
# Day 6 Sliding Window
# 567. Permutation in string

from typing import Counter

# Discussion 2 by Hieroglyphs, #3 rolling hash
# 60 ms, 93%; 14.2 mb, 87%
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        --3--
        [Accepted]
        [Runtime: 72 ms, faster than 57.45%]
        
        Enhanced freq dict - (Rolling hashmap)
        simiar problem: 438. Find All Anagrams in a String
        
            - instead of generating a fresh freq hashmap for every new substring
            - build the freq dict for the initial window and then slide the window_dict
              (add/remove chars) by adjusting their frequinces. 
              
              removing one preceding character and adding a new succeeding character to the new window
        '''
        k = len(s1)
        d1 = Counter(s1)
        
        # initial window
        window = s2[:k]
        d2 = Counter(window)
        
        # Check the initial window
        if d1 == d2:
            return True
        
        for i in range(len(s2) - k):
            # SLIDE THE WINDOW
            # 1 - remove s2[i]
            if d2[s2[i]] == 1:
                del d2[s2[i]]
            elif d2[s2[i]] > 1:
                d2[s2[i]] -= 1
                
            # 2 - add s2[i+k]
            if s2[i+k] in d2:
                d2[s2[i+k]] += 1
            else:
                d2[s2[i+k]] = 1
                
            # check after sliding
            if d1 == d2:
                return True
        return False


# Discussion 1 by ParthitPatel, sliding window
# 1448 ms, 32%; 14.5 mb, 9%
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        window = len(s1)
        s1_c = Counter(s1)
        for i in range(len(s2) - window + 1):
            s2_c = Counter(s2[i:i+window])
            if s2_c == s1_c:
                return True
        return False