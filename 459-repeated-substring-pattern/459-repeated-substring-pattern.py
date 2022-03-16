class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
    
        str1 = ""

        for i in range(1,len(s)):
            str1 = s[:i]
            if str1*(n//len(str1)) == s and n%len(str1) == 0:
                return True

        return False