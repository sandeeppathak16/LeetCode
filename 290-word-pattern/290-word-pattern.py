class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        s=s.split(' ')
        
        if len(s)!=len(pattern):
            return False
        
        if len(set(s))!=len(set(pattern)):
            return False
        
        d={}
        res=[]
        
        for i in range(len(s)):
            if pattern[i] not in d:
                d[pattern[i]]=s[i]
            res.append(d[pattern[i]])
            
        return res==s
        
        
        
        