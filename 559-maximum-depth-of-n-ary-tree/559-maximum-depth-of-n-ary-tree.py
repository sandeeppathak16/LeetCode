"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        ans = 0
        
        for child in root.children:
            temp = self.maxDepth(child)
            ans = max(ans, temp)
        return ans+1
        