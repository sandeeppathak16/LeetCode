class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        
        res =[]
        for ele in nums:
            count = 0
            for i in range(len(nums)):
                if ele>nums[i]:
                    count+=1
            res.append(count)
        return res