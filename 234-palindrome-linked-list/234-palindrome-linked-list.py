# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        p = None 
        c=head
        while head :
            if p is None:
                p = ListNode(head.val)
            else:
                node = ListNode(head.val)
                node.next=p
                p=node
            head = head.next
        
        while c:
            if c.val!=p.val:
                return False
            c=c.next
            p=p.next
        return True