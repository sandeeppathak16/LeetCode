class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        low=0
        high=len(nums)-1
        res=nums[low]
        
        while low<=high:
            if nums[low]<nums[high]:
                res=min(res, nums[low])
                break
            
            mid=(low+high)//2
            res=min(res, nums[mid])
            if nums[mid]>=nums[low]:
                low=mid+1
            else:
                high=mid-1
        return res
        
                
        
                
        