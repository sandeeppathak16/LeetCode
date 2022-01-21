class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x <0:
            return False
        p=r = 0
        
        num=x
        while x >0:
            r = x%10
            x=x//10
            p=p*10 + r
        if p==num:
            return True
        return False
            
            