class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('inf')
        
        nums = sorted(nums)
        summ=0
        
        for i in range(len(nums)):
            j = i+1
            k= len(nums)-1
            
            while j<k:
                
                summ = nums[i]+nums[j]+nums[k]
                dist = abs(target-summ)
                
                if summ == target:
                    return summ
                
                if abs(target-diff) > abs(target-summ):
                    diff = summ
                
                if summ>target:
                    k-=1
                else:
                    j+=1
                    
        return diff
                
                