#User function Template for python3

class Solution:
    #Complete this function
    # Function to find the maximum index difference.
    def maxIndexDiff(self,arr, N): 
        ##Your code here
        maxres = 0
        lmin=[0]*N
        rmax=[0]*N
        lmin[0]=arr[0]
        
        for i in range(1, N):
            lmin[i]=min(arr[i], lmin[i-1])
        
        rmax[N-1] = arr[N-1]
        
        for i in range(N-2, -1, -1):
            rmax[i] = max(arr[i], rmax[i+1])
            
        i=0
        j=0
        res=-1
        while i<N and j<N:
            if lmin[i]<=rmax[j]:
                maxres=max(maxres, j-i)
                j+=1
            else:
                i+=1
        return maxres
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            ob=Solution()
            print(ob.maxIndexDiff(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends