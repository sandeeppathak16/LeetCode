class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums = sorted(nums)
        res = set()
        
        for i in range(len(nums)):
            new_target = target-nums[i]
            
            for j in range(i+1, len(nums)):
                next_target = new_target-nums[j]

                k = j+1
                l=len(nums)-1

                while k < l:
                    summ= nums[k]+nums[l]

                    if summ > next_target:
                        l-=1
                    elif summ<next_target:
                        k+=1

                    else:
                        res.add((nums[i], nums[j], nums[k],nums[l]))
                        k+=1
                        l-=1
        return res