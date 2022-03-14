class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        
        nums.sort()
        return nums[-k]
#         def help(nums, k):
#             i=0
#             for j in range(len(nums)-1, -1, -1):
#                 if nums[j]!=nums[j-1]:
#                     i+=1
#                     if i==k:
#                         return nums[j]
        
        
        
#         if len(nums)==1 or len(nums)==2:
#             return max(nums)
        
#         res=help(nums)
            
#         if res==None:
#             return max(nums)
#         else:
        return help(nums, k)