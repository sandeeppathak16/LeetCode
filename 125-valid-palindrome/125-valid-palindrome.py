class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''.join(c for c in s if c.isalnum())
        new_s=new_s.lower()
        reverse_s=new_s[::-1]
        if new_s == reverse_s:
            return True
        else:
            return False