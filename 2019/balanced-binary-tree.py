# https://leetcode.com/problems/balanced-binary-tree/

"""
Given a binary tree, determine if it is height-balanced. For this problem, a height-balanced binary tree is defined as:
a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:
Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7

Return true.
"""
  
  
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        
        obtain depth of left and right subtrees and compare them (are they within +-1 of each other)
        """
        if root:
          left = isBalanced(root.left)
          right = isBalanced(root.right)
          if left == right or abs(left - right) <= 1:
            return True
          else:
            return False
        
