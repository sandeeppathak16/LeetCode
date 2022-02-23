# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res=[]
        str_node=''
        
        def help(tree, res, str_node):
            if tree is None:
                return
            if tree.right == None and tree.left == None:
                str_node+=str(tree.val)
                res.append(str_node)
                return
            
            str_node+=f'{tree.val}->'
            if tree.left:
                help(tree.left, res, str_node)
            if tree.right:
                help(tree.right, res, str_node)
    
            
            
            
        help(root, res, str_node)
        return res