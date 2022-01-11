# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = head
        count = 0
        while start is not None:
            start = start.next
            count +=1
        if count == 1:
            head = None
            return head
        if count%2 ==0:
            c = 1
            start_1 =head
            while c < ((count/2)):
                start_1 = start_1.next
                c+=1
            start_1.next = start_1.next.next
            return head
        else:
            c =1
            start_1 = head
            while c < ((count//2)):
                start_1 = start_1.next
                c+=1
            start_1.next = start_1.next.next
            return head