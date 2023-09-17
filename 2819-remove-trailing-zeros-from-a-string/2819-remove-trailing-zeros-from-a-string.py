class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        l = 0
        r = 0
        ln = len(num)

        for i in range(ln):
            if num[i] != '0':
                break
            
            l+=1
        

        for j in range(ln-1, -1, -1):
            if num[j] != '0':
                break
            
            r+=1
        
        if l:
            num = num[l:]
        if r:
            num = num[:ln - r]

        return num