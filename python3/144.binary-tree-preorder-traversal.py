# Data Structure Study Plan I
# Day 10
# 144. Binary tree preorder traversal (Easy)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Discussion 1 (by codeywodey) - runtime optimal (20 ms, 99%; 14.3 mb, 46%)
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        order, stack = [], [root]
        while stack:
            node = stack.pop()
            order.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return order


# Discussion 2, a variant of discussion 1 (by slayu) (28 ms, 85%; 14.2 mb, 75%)
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        res = []
        
        while stack:
            node = stack.pop()
            if not node:
                continue
                
            res.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
        
        return res


# Solution 2, Morris traversal - space optimal (32 ms, 62%; 14 mb, 99%)
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        node, output = root, []
        while node:
            if not node.left:
                output.append(node.val)
                node = node.right
            else:
                predecessor = node.left
                
                while predecessor.right and predecessor.right is not node:
                    predecessor = predecessor.right
                
                if not predecessor.right:
                    output.append(node.val)
                    predecessor.right = node
                    node = node.left
                else:
                    predecessor.right = None
                    node = node.right
        return output


# Solution 1, iterations (28 ms, 85%; 14.3 mb, 13%)
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Push nodes into output list following the order
        #  Top -> Bottom and Left -> Right, that naturally
        #  produces preorder traversal
        if root is None:
            return []
        
        stack, output = [root, ], []
        
        while stack:
            root = stack.pop()
            if root is not None:
                output.append(root.val)
                if root.right is not None:
                    stack.append(root.right)
                if root.left is not None:
                    stack.append(root.left)
        
        return output
## Time = O(N) - we visit each node exactly once, thus the time complexity is O(N), where N is the number of nodes, i.e. the size of tree.
## Space = O(N) - depending on the tree structure, we could keep up to the entire tree, therefore, the space complexity is O(N).