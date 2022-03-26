class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        def help(l, h, arr, x):
            
            if arr[h]<=x:
                return h
            if arr[l]>x:
                return l
            
            mid=(l+h)//2
            
            if arr[mid]<=x and arr[mid+1]>x:
                return mid
            if arr[mid]<x:
                return help(mid+1, h, arr, x)
            return help(l, mid-1, arr, x)
        
        l=help(0, len(arr)-1, arr, x)
        
        res=[]
        r=l+1
        
        # if arr[l]==x:
        #     l-=1
            
        count=0
        
        while l>=0 and r<len(arr) and count<k:
            if x-arr[l]<=arr[r]-x:
                res.append(arr[l])
                l-=1
                count+=1
            else:
                res.append(arr[r])
                r+=1
                count+=1
                
        while l>=0 and count<k:
            res.append(arr[l])
            l-=1
            count+=1
            
        while r<len(arr) and count<k:
            res.append(arr[r])
            r+=1
            count+=1
            
        return sorted(res)
            
                
                