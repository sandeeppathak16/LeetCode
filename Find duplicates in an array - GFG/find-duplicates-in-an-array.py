class Solution:
    def duplicates(self, arr, n): 
    	# code here
    	d={}
    	
    	res=[]
    	
    	for i in range(0, n):
            index = arr[i] % n
            arr[index] += n
    	    
    	for i in range(0, n):
            if (arr[i]/n) >= 2:
                res.append(i)
        
        if len(res)==0:
            return {-1}
        else:
            return res

    	
    	
    	
    	
    	    

#{ 
#  Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends