# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        count = 0
        start = head
        while start is not None:
            start = start.next
            count += 1
        print(count)
        if count%2 ==0:
            c = 1
            start_1 = head
            while c < (count//2)+1:
                start_1 = start_1.next
                c+=1
            return start_1
        else:
            c = 1
            start_1 = head
            while c <= (count//2):
                start_1 = start_1.next
                c+=1
            return start_1