# Data Structure Study Plan I
# Day 6
# 383. Ransom note (Easy)


# Solution 4, sorting and stacks (128 ms, 9%; 14.7 mb, 11%)
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine): return False
        
        # Reverse sort the note and magazine; treat list as a stack
        ransomNote = sorted(ransomNote, reverse=True)
        magazine = sorted(magazine, reverse=True)
        
        # While there are letters left on both stacks:
        while ransomNote and magazine:
            # If the tops are the same, pop both because we have found a match.
            if ransomNote[-1] == magazine[-1]:
                ransomNote.pop()
                magazine.pop()
            # If magazine's top is earlier in the alphabet, we should remove that 
            # character of magazine as we definitely won't need that letter.
            elif magazine[-1] < ransomNote[-1]:
                magazine.pop()
                # Otherwise, it's impossible for top of ransomNote to be in magazine.
            else:
                return False
        
        # Return true iff the entire ransomNote was built.
        return not ransomNote
## m = length of magazine; n = length of ransomNote; k = number of unique characters in both
## Time = O(m log m)
## Space = O(m)


# Solution 3, one HashMap (52 ms, 74%; 14.4 mb, 64%)
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine): return False
        
        letters = collections.Counter(magazine)
        
        for c in ransomNote:
            if letters[c] <= 0:
                return False
            letters[c] -= 1
        
        return True
## m = length of magazine; n = length of ransomNote; k = number of unique characters in both
## Time = O(n) = O(m)
## Space = O(k) / O(1)

# Solution 2, two HashMaps (48 ms, 83%; 14.3 mb, 64%)
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine): return False
        
        mag_counts = collections.Counter(magazine)
        rans_counts = collections.Counter(ransomNote)
        
        for char, count in rans_counts.items():
            mag_ct = mag_counts[char]
            if mag_ct < count:
                return False
        return True
## m = length of magazine; n = length of ransomNote; k = number of unique characters in both
## Time = O(n)+O(n)+O(m) = O(m)+O(m)+O(m) = 3⋅O(m) = O(m)
## Space = O(k) / O(1)


# Solution 1, simulation (40 ms, 92%; 14.5 mb, 36%)
# This is fast because test cases are small; need optimal alternatives
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for c in ransomNote:
            if c not in magazine:
                return False
            location = magazine.index(c)
            # Use splicing to make a new string with the characters
            #  before "location" (but not including), and the characters
            #  after "location"
            magazine = magazine[:location] + magazine[location+1:]
        return True
## m = length of magazine; n = length of ransomNote; k = number of unique characters in both
## Time = n ⋅ O(m) = O(m ⋅ n)
## Space = O(m)


# (new) approach 1, brute force w/ hashmap (92 ms, 22%; 14.2 mb, 86%)
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        mag_dict = {}
        # create a dictionary for every letter in magazine
        for i in range(len(magazine)):
            if magazine[i] not in mag_dict:
                mag_dict[magazine[i]] = 1
            else:
                mag_dict[magazine[i]] += 1
        # check letters in ransomNote
        for j in range(len(ransomNote)):
            if ransomNote[j] not in mag_dict:
                return False
            else:
                if mag_dict[ransomNote[j]] == 1:
                    mag_dict.pop(ransomNote[j])
                else:
                    mag_dict[ransomNote[j]] -= 1
        return True


# (new) approach 2, brute force by converting to array (1584 ms, 5%; 14.4 mb, 36%)
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        # sort to convert string to array
        rans = sorted(ransomNote)
        mag = sorted(magazine)
        for letter in rans:
            if letter not in mag:
                return False
            else:
                mag.remove(letter)
        return True