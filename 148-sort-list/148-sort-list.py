# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        value=[]
        
        temp=head
        
        while temp:
            value.append(temp.val)
            temp=temp.next
            
        value.sort()
        temp=head
        i=0
        while temp and i<len(value):
            temp.val=value[i]
            temp=temp.next
            i+=1
        return head
        