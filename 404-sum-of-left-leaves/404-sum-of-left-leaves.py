# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
    
        def help(tree, ll):
            if tree is None:
                return 0
            if tree.left == None and tree.right ==None and ll:
                return tree.val
            add_l=help(tree.left, True)
            add_r=help(tree.right, False)
            
            return add_l + add_r
            
        res = help(root, False)
        return res