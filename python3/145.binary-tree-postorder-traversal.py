# Data Structure Study Plan I
# Day 10
# 145. Binary tree postorder travesal (Easy)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Approach 2 (by OldCodingFarmer) - iteratively (28 ms, 86%; 14.1 mb, 77%)
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return res[::-1]


# Approach 1 (by OldCodingFarmer) - recursively (28 ms, 86%; 14.3 mb, 13%)
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:       
        res = []
        self.dfs(root, res)
        return res
    def dfs(self, root, res):
        if root:
            self.dfs(root.left, res)
            self.dfs(root.right, res)
            res.append(root.val)