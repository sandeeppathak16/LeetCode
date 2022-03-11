# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        l=[]
        while head:
            l.append(head.val)
            head=head.next
            
        l[k-1], l[len(l)-k]=l[len(l)-k], l[k-1]
        
        dummy = ListNode(l[0])
        res=dummy
        for i in range(1, len(l)):
            node = ListNode(l[i])
            dummy.next=node
            dummy=node
        return res
            