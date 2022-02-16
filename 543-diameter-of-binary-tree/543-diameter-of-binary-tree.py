# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:  
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.res = 0
        
        def diameter(root):
            l, r =0, 0
            if root is None:
                return 0
            if not root.left and not root.right:
                return 0
            if root.left or root.right:
                if root.left:
                    l = diameter(root.left)+1
                if root.right:
                    r = diameter(root.right)+1

                self.res = max(self.res, l+r)
                return max(l, r)
            
        diameter(root)
        return self.res
                
                
        
       
        