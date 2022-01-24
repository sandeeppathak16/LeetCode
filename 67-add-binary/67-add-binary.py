class Solution:
    def addBinary(self, a: str, b: str) -> str:
        add = ''
        new_a = int(a, 2)
        new_b = int(b, 2)

        res = new_a + new_b
        
        return bin(res)[2:]
                    
        
                
                
                
            