class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        numX= nums[:n]
        numY=nums[n:]
        
        res=[]
        for i in range(len(numX)):
            res.append(numX[i])
            res.append(numY[i])
        return res
        