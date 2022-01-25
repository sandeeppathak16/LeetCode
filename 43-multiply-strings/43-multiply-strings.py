class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        new_num1 = list(num1)
        new_num2 = list(num2)
        
        new_num1 = new_num1[::-1]
        
        new_num2 = new_num2[::-1]
        x , y = 0, 0
        
        while new_num1:
            x = x*10 + ord(new_num1.pop())-48
        while new_num2:
            y = y*10 + ord(new_num2.pop())-48
        return str(x*y)
                
            