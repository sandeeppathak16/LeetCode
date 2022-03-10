# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # stack=[]
        # result=False
        # while head:
        #     if head.val in stack:
        #         result=True
        #         break
        #     stack.append(head.val)
        #     head=head.next
        # return result
        
        if head is None:
            return False
        
        fast=slow=head
        
        while fast.next!=None and fast.next.next!=None:
            fast=fast.next.next
            slow=slow.next
            if slow==fast:
                return True
            
        return False
                