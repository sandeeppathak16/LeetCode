class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        L = len(nums)
        n = L//2
        index = -1
        if target > nums[n]:
            for i in range(n, L):
                if nums[i]==target:
                    index = i
        else:
            for i in range(0, n+1):
                if nums[i]==target:
                    index = i
        return index 
        