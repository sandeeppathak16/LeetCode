#User function Template for python3


# arr[] : the input array containing 0s and 1s
# N : size of the input array

# return the maximum length of the subarray
# with equal 0s and 1s
class Solution:
    def maxLen(self,arr, N):
        # code here
        
        d={}
        summ=0
        max_len=0
        
        for i in range(len(arr)):
            if arr[i]==0:
                arr[i]=-1
                
            summ+=arr[i]
            
            if summ==0:
                max_len=i+1
            if summ in d:
                max_len = max(max_len, i-d[summ])
                
            else:
                d[summ]=i
        return max_len

#{ 
#  Driver Code Starts
#Initial Template for Python 3


t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().maxLen(a, len(a))
    print(s)
# } Driver Code Ends