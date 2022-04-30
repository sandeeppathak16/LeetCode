class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        hashmap={}
        res=[]
        
        for ele in nums:
            if ele not in hashmap:
                hashmap[ele]=1
            else:
                hashmap[ele]+=1
        for key in hashmap:
            if hashmap[key] > (len(nums)/3):
                
                res.append(key)
                print(res)
        return res