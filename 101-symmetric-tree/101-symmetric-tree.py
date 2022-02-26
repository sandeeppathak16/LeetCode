# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def mirror(left, right):
            if left == None and right == None:
                return True
            elif left == None or right == None:
                return False
            elif left.val != right.val:
                return False
            
            return mirror(left.left, right.right) and mirror(left.right, right.left)
        
        if root is None:
            return True
        return mirror(root.left, root.right)