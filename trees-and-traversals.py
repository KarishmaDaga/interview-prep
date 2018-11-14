# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
    
    # tree traversals
    
    # inorder traversal
    def inorder(root):
        inorder(root.left)
        print(root.val)
        inorder(root.right)
   
   # preorder traversal
   def preorder(root):
      print(root.val)
      preorder(root.left)
      preorder(root.right)
   
   # postorder traversal
   def postorder(root):
      postorder(root.left)
      postorder(root.right)
      print(root.val)
      
