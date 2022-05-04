#User function Template for python3
class Solution:
    def sortArr(self, arr, n): 
        
        
        #code here
        
        def partition(arr, low, high):
            pivote_index=low
            pivote = arr[pivote_index]
            
            while low<high:
                while low<len(arr) and arr[low]<=pivote:
                    low+=1
                while arr[high]>pivote:
                    high-=1
                if low<high:
                    arr[low], arr[high] = arr[high], arr[low]
            arr[pivote_index], arr[high] = arr[high], arr[pivote_index]
            return high
            
        
        def quicksort(arr, low, high):
            
            if low<high:
                pi=partition(arr, low, high)
                quicksort(arr, low, pi-1)
                quicksort(arr, pi+1, high)
        quicksort(arr, 0, len(arr)-1)
        return arr
            
                    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        obj = Solution()
        ans = obj.sortArr(arr, n)
        for i in ans:
            print(i,end=" ")
        print()
# } Driver Code Ends