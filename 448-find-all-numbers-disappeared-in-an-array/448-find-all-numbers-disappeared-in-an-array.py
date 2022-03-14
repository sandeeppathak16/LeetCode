class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        check=Counter(nums)
        
        res=[]
                
        for i in range(1, len(nums)+1):
            if i not in check.keys():
                res.append(i)
                
        return res
                
        