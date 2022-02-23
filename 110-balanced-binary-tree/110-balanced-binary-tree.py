# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def help(tree):
            if tree == None:
                return (0, True)
            
            lt=help(tree.left)
            rt=help(tree.right)
            
            diff = abs(lt[0]-rt[0])<=1
            
            height = 1 +max(lt[0], rt[0])
            
            return height , lt[1] and rt[1] and diff
        
        return help(root)[1]
        