# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        
        
        def merge(list_1, list_2):
            prev = 0
            x = ListNode(0)
            y = x
            while list_1 and list_2:
                if list_1:
                    if list_1.val > list_2.val:
                        y.next = list_2
                        list_2 = list_2.next
                    else:
                        y.next = list_1
                        list_1 = list_1.next
                    y = y.next
                else:     
                    if list_1.val < list_2.val:
                            y.next = list_1
                            list_2 = list_1.next
                    else:
                        y.next = list_2
                        list_2 = list_2.next
                    y = y.next
            if list_1:
                y.next = list_1
            else:
                y.next = list_2
            return x.next
        
#         def sort(link):
            
#             current=link
#             index=None
            
#             while current!=None:
#                 index=current.next
#                 while index!=None:
#                     if current.val>index.val:
#                         temp=current.val
#                         current.val=index.val
#                         index.val=temp
#                     index=index.next
#                 current=current.next
#             return link
            
        
        if len(lists)==0:
            return
        if len(lists)==1:
            return (lists[0])
        
        
        result_link = lists[0]
        
        
                
            
        for i in range(1,len(lists)):
            result_link= merge(result_link, lists[i])
        
        return result_link