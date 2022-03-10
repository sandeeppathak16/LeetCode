# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a=0
        while l1!=None:
            a=a*10+l1.val
            l1=l1.next
        
        b=0
        while l2!=None:
            b=b*10+l2.val
            l2=l2.next
        add=a+b
        
        curr=None
        if add==0:
            curr=ListNode(0)
            return curr
        while add!=0:
            node=ListNode(add%10, None)
            node.next=curr
            curr=node
            add=add//10
        
        return curr
        