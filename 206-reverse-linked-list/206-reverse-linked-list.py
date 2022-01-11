# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = None
        while head:
            if dummy_head is None:
                dummy_head = ListNode(head.val)
            else:
                node = ListNode(head.val)
                node.next = dummy_head
                dummy_head = node
            head = head.next
        return dummy_head