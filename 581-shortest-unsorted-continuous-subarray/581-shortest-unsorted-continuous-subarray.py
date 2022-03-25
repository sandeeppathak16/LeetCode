class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        s=e=0
        if len(nums)==1:
            return 0
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                s=i
                break
            elif i==len(nums)-2:
                return 0
        # if s == 0:
        #     return 0
        j=len(nums)-1
        while j>0:
            if nums[j]<nums[j-1]:
                e=j
                break
            j-=1
        max_x=max(nums[s:e+1])
        min_x=min(nums[s:e+1])
        
        for i in range(s):
            if min_x<nums[i]:
                s=i
                break
        i=len(nums)-1
        while i>=e+1:
            if max_x>nums[i]:
                e=i
                break
            i-=1
            
        return e-s+1