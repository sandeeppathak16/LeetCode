class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = list(num1)
        num2 = list(num2)
        num1.reverse()
        num2.reverse()
        x,y = 0,0
        
        while num1:
            x = x*10 + ord(num1.pop())-48
        while num2:
            y = y*10 + ord(num2.pop())-48
        
        return str(x+y)
            
        