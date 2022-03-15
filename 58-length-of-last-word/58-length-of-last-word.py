class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        
        l= len(s)-1
        
        space=''
        while l>=0:
            if s[l].isalpha():
                break
            else:
                l-=1
                
        res=''
        
        while l>=0:
            if s[l].isalpha():
                res+=s[l]
                l-=1
            else:
                break
                
        return len(res)