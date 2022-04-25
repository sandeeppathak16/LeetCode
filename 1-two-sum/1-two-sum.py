class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numHashMap = {}
        for i, num in enumerate(nums):
            if target-num in numHashMap:
                return [numHashMap[target-num], i]
            numHashMap[num] = i