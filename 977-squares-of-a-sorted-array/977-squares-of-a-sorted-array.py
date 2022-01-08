class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i=0
        for item in nums:
            nums[i]=item * item
            i +=1
        nums.sort()
        return nums
        