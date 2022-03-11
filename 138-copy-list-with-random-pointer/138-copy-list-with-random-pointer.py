"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        map = {}
        dummy= Node(100001)
        curr=head
        runner=dummy
        
        while curr!=None:
            node = Node(curr.val)
            runner.next=node
            map[curr]=node
            curr=curr.next
            runner=runner.next
        
        print(map)
            
        curr=head
        runner=dummy.next
        
        while curr!=None:
            if curr.random!=None:
                runner.random=map[curr.random]
            runner=runner.next
            curr=curr.next
        return dummy.next
        
        