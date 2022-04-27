#User function Template for python3

class Solution:
    
    #Function to count subarrays with 1s and 0s.
    def countSubarrWithEqualZeroAndOne(self,arr, n):
        #Your code here
        
        hashmap={}
        
        sum=0
        count=0
        
        for a in arr:
            if a==0:
                a = -1
            sum+=a
            
            if sum==0:
                count+=1
            count+=hashmap.get(sum,0)
            hashmap[sum]=1+hashmap.get(sum,0)
        return count
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3



def main():
    T=int(input())
    while(T>0):
        
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        
        obj = Solution()
        print(obj.countSubarrWithEqualZeroAndOne(arr, n))
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends