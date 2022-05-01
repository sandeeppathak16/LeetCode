class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hashmap={}
        summ=0
        max_len=0
        
        for i in range(len(nums)):
            if nums[i]==0:
                nums[i]=-1
                
            summ+=nums[i]
            if summ==0:
                max_len=i+1
                
            if summ in hashmap:
                max_len=max(max_len, i-hashmap[summ])
            else:
                hashmap[summ]=i
        return max_len