class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
       
    
        d={}
        count=0
        
        
        for ele in nums:
            d[ele]=d.get(ele, 0)+1
            
        if k==0:
            for key in d:
                if d[key]>1:
                    count+=1
        else:
            for key in d:
                if (key+k) in d:
                    count+=1
        return count
                
            
            