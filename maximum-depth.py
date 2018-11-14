# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        To det max depth, I need to perform DFS on the binary tree.
        Depth of a BT is the max path from a node to a leaf node.
        I can perform inorder traversal and keep counter of depth.
        Since BT has at most two children, I can have depth of left 
        subtree and right subtree counters and compare them at the end.
        """
        depth = 0
        
        if root is None:
            return 0
        else:
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
        return max(left_height, right_height) + 1
        

        
