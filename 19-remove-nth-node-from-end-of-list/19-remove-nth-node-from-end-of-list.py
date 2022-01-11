# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        second = head
        count =0
        for i in range(n):
            if(second.next == None):
                if(i == n - 1):
                    head = head.next
                return head
            second = second.next
         
        while(second.next != None):
            second = second.next
            first = first.next
        while second.next is not None:
            second = second.next
            first = first.next
        first.next = first.next.next
        return head