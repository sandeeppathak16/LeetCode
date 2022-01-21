class Solution:
    def validPalindrome(self, s: str) -> bool:
        l= len(s)
        
        for i in range(l):
            if s[i]!=s[l-i-1]:
                a=s[:i]+s[i+1:]
                l=len(a)
                if a==a[::-1]:
                    return True
                else:
                    b = s[:l-i]+s[l-i+1:]
                    l=len(b)
                    if b == b[::-1]:
                        return True
                    else:
                        return False
        return s == s[::-1]