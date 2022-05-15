#User function Template for python3

class Solution:
    def sumClosest(self, arr, x):
        # code here
        
        i=0
        j=len(arr)-1
        diff=float('inf')
        res=[]
        res_l=0
        res_r=0
        
        while i<j:
            summ=arr[i]+arr[j]
            
            if abs(x-summ)<diff:
                res_l=i
                res_r=j
                diff=abs(x-summ)
                
            if summ>x:
                j-=1
            else:
                i+=1
        return (arr[res_l], arr[res_r])
            
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.sumClosest(arr, x)
        print(str(ans[0]) + " " + str(ans[1]))
        tc -= 1
# } Driver Code Ends