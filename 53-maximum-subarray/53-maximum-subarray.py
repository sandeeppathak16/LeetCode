class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum=nums[0]
        
        currsum=0
        
        for ele in nums:
            if currsum<0:
                currsum=0
            currsum+=ele
            maxsum=max(maxsum, currsum)
            
        return maxsum