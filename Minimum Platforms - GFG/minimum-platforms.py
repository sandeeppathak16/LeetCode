#User function Template for python3

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        # code here
        
        arr.sort()
        dep.sort()
        
        i, j, mp, np = 1, 0, 1, 1
        
        while i<=n-1 and j<=n-1:
            if dep[j]<arr[i]:
                j+=1
                mp-=1
            else:
                i+=1
                mp+=1
            np=max(np, mp)
            
        return np

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        arrival = list(map(int, input().strip().split()))
        departure = list(map(int, input().strip().split()))
        ob=Solution()
        print(ob.minimumPlatform(n,arrival,departure))
# } Driver Code Ends