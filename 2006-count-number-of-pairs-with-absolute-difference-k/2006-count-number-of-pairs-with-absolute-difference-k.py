class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        
        hashmap={}
        count=0
        
        for i in range(len(nums)):
            if (nums[i]-k) in hashmap:
                count+=hashmap[nums[i]-k]
            if (nums[i]+k) in hashmap:
                count+=hashmap[nums[i]+k]
            hashmap[nums[i]]=1+hashmap.get(nums[i], 0)
        return count
        