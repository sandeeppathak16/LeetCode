#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr, n):
		# code here
		currprod=1
		maxprod=float('-inf')
		
		for i in range(0, n):
		    currprod=currprod*arr[i]
		    
		    maxprod=max(currprod, maxprod)
		    if currprod==0:
		        currprod=1
		currprod=1
		for i in range(n-1, -1, -1):
		    currprod=currprod*arr[i]
		    
		    maxprod=max(currprod, maxprod)
		    if currprod==0:
		        currprod=1
		return maxprod
		

#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends