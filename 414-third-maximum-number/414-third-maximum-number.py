class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        
        nums.sort()
        def help(nums):
            i=0
            for j in range(len(nums)-1, -1, -1):
                if nums[j]!=nums[j-1]:
                    i+=1
                    if i==3:
                        return nums[j]
        
        
        
        if len(nums)==1 or len(nums)==2:
            return max(nums)
        
        res=help(nums)
            
        if res==None:
            return max(nums)
        else:
            return res
        