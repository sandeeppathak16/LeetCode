# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a=b=head
        
        iscycle=False
        
        if head == None:
            return None
        if head.next == None:
            return None
        
        while b.next!=None and b.next.next!=None:
            b=b.next.next
            a=a.next
            if a==b:
                iscycle=True
                break
        if iscycle:
            s=head
            while a!=s:
                a=a.next
                s=s.next
            return s
        return None
        
        