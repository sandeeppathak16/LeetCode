class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums)-1
        
        if target not in nums:
            return -1
        else:
            return nums.index(target) 