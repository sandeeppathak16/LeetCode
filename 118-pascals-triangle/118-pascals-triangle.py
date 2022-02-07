class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        from math import factorial
        res =[]
        
        for r in range(numRows):
            r_res =[]
            for c in range(r+1):
                num = factorial(r)//(factorial(c)*factorial(r-c))
                r_res.append(num)
            res.append(r_res)
        return res
            
        