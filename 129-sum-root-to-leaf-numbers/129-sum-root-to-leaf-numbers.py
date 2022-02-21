# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def dfs(tree, sum):
            if not tree:
                return 0
            sum = 10 * sum + tree.val
            if not tree.right and not tree.left:
                return sum

            return dfs(tree.left, sum) + dfs(tree.right, sum)
            
        res = dfs(root, 0)
        return res