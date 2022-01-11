# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        
        while fast:
            
            slow = slow.next
            fast = fast.next
            
            if fast:
                fast = fast.next
                
        
        prev, cur = None, slow
        
        while cur:
            
            next_hop = cur.next
            cur.next = prev
            prev = cur
            cur = next_hop
            
        
        left, right = head, prev
        max_sum = -1
        
        while left and right:
            max_sum = max( max_sum, left.val + right.val)
            left, right = left.next, right.next
            
        return max_sum