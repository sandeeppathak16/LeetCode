"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        self.l=[]
        
        def help(root):
            if root:
                self.l.append(root.val)
                for child in root.children:
                    c = help(child)
        help(root)
        return self.l
            
        