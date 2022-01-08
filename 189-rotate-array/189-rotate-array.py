class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        if k <= len(nums):
            nums[:]=nums[len(nums)-k:]+nums[:len(nums)-k]
        else:
            k2=k%len(nums)
            nums[:]=nums[len(nums)-k2:]+nums[:len(nums)-k2]