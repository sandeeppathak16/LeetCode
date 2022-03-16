class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d=Counter(t)
        
        for l in s:
            d[l]-=1
        res=''
        for key in d.keys():
            if d[key]>0:
                res+=key
        
        return res