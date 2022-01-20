class Solution:
    def fun(self,n,i):
        p=pow(2,i)
        if(p==n):
            return True
        else:
            if(p>n):
                return False
        return self.fun(n,i+1)

        
    def isPowerOfTwo(self, n: int) -> bool:
        return self.fun(n,0)