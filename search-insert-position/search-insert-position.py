class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(0, len(nums)):
            if nums[i] == target:
                return i
            for j in range(i+1, len(nums)):
                if target < nums[j] and target > nums[j-1]:
                    return j
            if target > max(nums):
                return len(nums)
            if target == 0:
                return 0
            if target < min(nums):
                return 0
        