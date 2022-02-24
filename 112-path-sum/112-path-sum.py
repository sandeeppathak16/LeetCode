# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        
        def help(tree, sum, target):
            if tree is None:
                return False
            if tree.left == None and tree.right == None:
                sum = sum + tree.val
                return sum==target
                    
            sum = sum + tree.val  
            
            return help(tree.left, sum, target) or help(tree.right, sum, target)
            
            
        return help(root, 0, targetSum)
            
                