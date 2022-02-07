class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        
        res =[]
        for i in range(len(nums)):
            sum = 0
            for j in range(i+1):
                sum = sum +nums[j]
            res.append(sum)
        return res