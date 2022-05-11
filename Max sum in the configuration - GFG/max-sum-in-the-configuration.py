#User function Template for python3

def max_sum(a,n):
    #code here
    
    cum_sum=0
    curr_val=0
    
    for i in range(0, n):
        cum_sum+=a[i]
        curr_val+=i*a[i]
    res=curr_val
    
    for i in range(1, n):
        next_val=curr_val - (cum_sum - a[i-1]) + a[i-1]*(n-1)
        
        curr_val=next_val
        
        res=max(res, next_val)
        
    return res
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3


    
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(max_sum(arr,n))
# } Driver Code Ends