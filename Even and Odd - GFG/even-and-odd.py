#User function Template for python3

class Solution:
    def reArrange(self, arr, N):
        # code here 
        even_list=[]
        odd_list=[]
        
        for ele in arr:
            if ele%2==0:
                even_list.append(ele)
            else:
                odd_list.append(ele)
                
        
        j=k=0
        for i in range(len(arr)):
            if i%2==0:
                arr[i]=even_list[j]
                j+=1
            else:
                arr[i]=odd_list[k]
                k+=1
        return arr

#{ 
#  Driver Code Starts
#Initial Template for Python 3


def check(arr, n):
    flag = 1
    c=d=0
    for i in range(n):
        if i%2==0:
            if arr[i]%2:
                flag = 0
                break
            else:
                c+=1
        else:
            if arr[i]%2==0:
                flag = 0
                break
            else:
                d+=1
    if c!=d:
        flag = 0
            
    return flag
        
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        ob.reArrange(arr,N)
        
        print(check(arr,N))

# } Driver Code Ends