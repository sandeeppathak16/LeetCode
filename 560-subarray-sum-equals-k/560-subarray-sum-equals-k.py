class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res=0
        currSum=0
        prefixsum={0 : 1}
        
        for n in nums:
            currSum+=n
            diff = currSum-k
            
            res+=prefixsum.get(diff, 0)
            prefixsum[currSum]=1+prefixsum.get(currSum, 0)
        return res