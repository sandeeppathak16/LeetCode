class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
            
        }
        
        sum = roman[s[len(s)-1]]
        i=len(s)-2
        
        while i >=0:
            if roman[s[i]]<roman[s[i+1]]:
                sum = sum - roman[s[i]]
                i = i - 1
            else:
                sum = sum + roman[s[i]]
                i = i-1
                
        
        return sum
            