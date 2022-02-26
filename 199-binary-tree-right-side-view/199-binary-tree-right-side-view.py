# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        result =[]
        s = set()
        def help(tree, result, s, level):
            if tree is None:
                return 
            
            if level not in s:
                s.add(level)
                result.append(tree.val)
            help(tree.right, result, s, level+1)
            help(tree.left, result, s, level+1)
            
        help(root, result, s, 0)
        return result