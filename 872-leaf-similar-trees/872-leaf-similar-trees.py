# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def help(tree, v):
            if tree is None:
                return None
            if tree.left == None and tree.right == None:
                v.append(tree.val)
            if tree.left != None:
                help(tree.left, v)
            if tree.right != None:
                help(tree.right, v)
            
            return v
        a =[]
        b=[]
        a = help(root1, a)
        b = help(root2, b)
        
        return a==b