def transitionPoint(arr, n):
    #Code here
    
    
    l=0
    r=n-1
    while l<=r:
        mid=(l+r)//2
        if arr[mid]==0:
            l=mid+1
        elif (arr[mid]==1 and arr[mid-1]==0 and mid>0) or mid==0:
            return mid
        else:
            r=mid-1
            
    return -1
        
#{ 
#  Driver Code Starts
#driver code
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(transitionPoint(arr, n))

# } Driver Code Ends