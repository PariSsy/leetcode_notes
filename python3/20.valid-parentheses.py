# Data Structure Study Plan I
# Day 9
# 20. Valid parentheses (Easy)
## Test case that I failed on the new round: "([)]"

# Discussion (by gangar) (28 ms, 87%; 14.1 mb, 87%)
class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {"(": ")", "[": "]",  "{": "}"}
        open_par = set(["(", "[", "{"])
        stack = []
        for char in s:
            if char in open_par:
                stack.append(char)
            elif stack and char == bracket_map[stack[-1]]:
                stack.pop()
            else:
                return False
        return stack == []


# Solution, stack (32 ms, 67%; 14.2 mb, 65%)
class Solution:
    def isValid(self, s: str) -> bool:
        # The stack to keep track of opening brackets.
        stack = []
        
        # Hash map for keeping track of mappings. This keeps the code very clean
        # Also makes adding more types of parenthesis easier
        mapping = {")":"(", "}":"{", "]":"["}
        
        # For every bracket in the expression
        for char in s:
            # If the character is an closing bracket
            if char in mapping:
                # Pop the topmost element from the stack, if it is not empty
                # Otherwise assign a dummy value of '#' to the top_element variable
                top_element = stack.pop() if stack else '#'
                # The mapping for the opening bracket in out hash and the top
                # element of the stack don't match, return False
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack
                stack.append(char)
## Time = O(n) because we traverse the given string 1 character at a time; push & pop operations on a stack take O(1) time.
## Space = O(n) as we push all opening brackets onto the stack and in the worst case, we will end up pushing all the brackets onto the stack. e.g. ((((((((((



# (new) failed on test case "([)]"
class Solution:
    def isValid(self, s: str) -> bool:
        if s[0] in [")", "}", "]"]:
            return False
        counter = {")": 0, "}": 0, "]": 0}
        for char in s:
            if char in [")", "}", "]"]:
                counter[char] -= 1
                if counter[char] < 0:
                    return False
            if char == "(":
                counter[")"] += 1
            if char == "[":
                counter["]"] += 1
            if char == "{":
                counter["}"] += 1
        if max(counter.values()) != 0 or min(counter.values()) != 0:
            return False
        return True          