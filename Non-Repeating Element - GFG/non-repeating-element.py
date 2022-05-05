#User function Template for python3

class Solution:
    def firstNonRepeating(self, arr, n): 
        # Complete the function
        
        # for i in range(len(arr)):
        #     if arr[i] not in arr[:i] and arr[i] not in arr[i+1:]:
        #         return arr[i]
        # return 0
        from collections import Counter
        c = Counter(arr)
        for ele in arr:
            if c[ele]==1:
                return ele
        return 0

#{ 
#  Driver Code Starts
#Initial Template for Python 3

from collections import defaultdict 

for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.firstNonRepeating(arr, n))
    
# } Driver Code Ends