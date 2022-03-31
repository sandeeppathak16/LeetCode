#User function Template for python3
class Solution:
	def countTriplet(self, arr, n):
		# code here
		arr.sort()
		count=0
		i=n-1
		while i>=0:
		    j=0
		    k=i-1
		    
		    while j<k:
		        if arr[i]==arr[k]+arr[j]:
		            count+=1
		            k-=1
		            j+=1
		            
		        elif arr[i]>arr[k]+arr[j]:
		            j+=1
		        else:
		            k-=1
		    i-=1
		    
        return count

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		arr = [int(x) for x in input().split()]

		ob = Solution()
		ans = ob.countTriplet(arr, n)
		print(ans)

# } Driver Code Ends