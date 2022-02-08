class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        arr = [*range(l+1)]
        
        for i in range(len(arr)):
            if i not in nums:
                return i