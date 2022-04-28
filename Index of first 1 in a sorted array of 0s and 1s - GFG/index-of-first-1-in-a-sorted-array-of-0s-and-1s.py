#User function Template for python3

class Solution:
    def firstIndex(self, arr, n):
    # Your code goes here
    
        l, r = 0, n-1
        if arr[0]==1:
            return 0
        
        while l<=r:
            mid=(l+r)//2
            
            if arr[mid]==1 and arr[mid-1]==0:
                return mid
            elif arr[mid]==0:
                l=mid+1
            elif arr[mid-1]==1 and arr[mid]==1:
                r=mid-1
        return -1
                



#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.firstIndex(a, n))

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends