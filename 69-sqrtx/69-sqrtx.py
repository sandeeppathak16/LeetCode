class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x<=1:
            return x
        
        
        low =1
        high=x//2
        
        while high>=low:
            
            mid = low + (high-low)//2
            
            if mid*mid==x:
                return mid
            elif mid*mid <x:
                if (mid+1)**2>x:
                    return mid
                low=mid+1
            else:
                if (mid-1)**2<x:
                    return mid-1
                high = mid-1

                
        