# Data Structure Study Plan I
# Day 10
# 94. Binary tree inorder traversal (Easy)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Approach 2 (OldCodingFarmer) - iteratively (28 ms, 86%; 14.3 mb, 14%)
class Solution:
    def inorderTraversal(self, root):
        res, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right


# Approach 1 (OldCodingFarmer) - recursively (32 ms, 64%; 14.2 mb, 76%)
class Solution:
    def inorderTraversal(self, root):
        res = []
        self.helper(root, res)
        return res
    
    def helper(self, root, res):
        if root:
            self.helper(root.left, res)
            res.append(root.val)
            self.helper(root.right, res)