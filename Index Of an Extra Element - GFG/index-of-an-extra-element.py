class Solution:
    def findExtra(self,a,b,n):
        #add code here
        sum1=sum(a)
        sum2=sum(b)
        
        ele=abs(sum1-sum2)
        
        if ele in a:
            return a.index(ele)
        else:
            b.index(ele)

#{ 
#  Driver Code Starts
if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        print(Solution().findExtra(a,b,n))
# } Driver Code Ends