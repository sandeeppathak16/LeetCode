#User function Template for python3

class Solution:
    def findMin(self, arr, n):
        #complete the function here
        
        l=0
        r=n-1
        
        while l<r:
            mid=(r+l)//2
            if arr[mid]<arr[r]:
                r=mid
            else:
                l=mid+1
        return arr[l]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        print(ob.findMin(arr, n))
# } Driver Code Ends