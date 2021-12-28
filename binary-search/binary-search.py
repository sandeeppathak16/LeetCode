class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n= len(nums)//2
        index = -1
        if target > nums[n]:
            for i in range(n-1, len(nums)):
                if target == nums[i]:
                    index=i
                    break
            
        else:
            for i in range(0, n+1):
                if target == nums[i]:
                    index=i
                    break
        return index