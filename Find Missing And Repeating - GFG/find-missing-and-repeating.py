#User function Template for python3

class Solution:
    def findTwoElement( self,arr, n): 
        # code here
        ans=[]
        temp=[0]*(n+1)
        for i in range(n):
            if temp[arr[i]]==0:
                temp[arr[i]]=1
            else:
                ans.append(arr[i])
        for i in range(1, n+1):
            if temp[i] == 0:
                ans.append(i)
        return ans
            
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends