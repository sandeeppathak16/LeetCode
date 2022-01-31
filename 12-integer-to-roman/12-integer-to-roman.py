class Solution:
    def intToRoman(self, num: int) -> str:
        result = ''

        numerals = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
    
        for v in reversed(numerals):
            n = int(num / v)
            if n >= 1:
                result += (numerals[v] * n)
            num %= v
    
        return result
        
        