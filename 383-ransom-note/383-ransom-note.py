class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        s= Counter(magazine)
        
        for l in ransomNote:
            if l in s.keys():
                s[l]-=1
                if s[l]<0:
                    return False
            else:
                return False
        return True