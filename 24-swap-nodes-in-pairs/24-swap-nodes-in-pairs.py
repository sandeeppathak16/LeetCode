# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return
        if head.next==None:
            return head
        res=head
        
        while head!=None:
            if head.next:
                temp=head.val
                head.val=head.next.val
                head.next.val=temp

                head=head.next.next
            else:
                head=head.next
            
        
        return res
        
        
            

        