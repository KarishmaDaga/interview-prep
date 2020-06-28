# https://leetcode.com/problems/invert-binary-tree/
"""
  Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9

Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            # switch subtrees
            temp = root.left
            root.left = root.right
            root.right = temp
          
            # recurse on subtrees
            self.invertTree(root.left)
            self.invertTree(root.right)
            
        # return inverted tree  
        return root
        
        
        
        
        
        
        
        
        
        
        
        
