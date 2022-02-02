class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        
        res = set()
        summ = 0
        
        for i in range(len(nums)):
            target = -nums[i]
            
            j = i+1
            k=len(nums)-1
            
            while j < k:
                summ= nums[j]+nums[k]
                
                if summ > target:
                    k-=1
                elif summ<target:
                    j+=1
                    
                else:
                    res.add((nums[i], nums[j], nums[k]))
                    j+=1
                    k-=1
        return res
                