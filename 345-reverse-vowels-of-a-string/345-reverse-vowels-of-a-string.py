class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        found_vowels = "".join(c for c in s if c in vowels)[::-1]
        
        inx = 0
        final =''
        for c in s:
            if c in vowels:
                final+= found_vowels[inx]
                inx+=1
            else:
                final+=c
        return final