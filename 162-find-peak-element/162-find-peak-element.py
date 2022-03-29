class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        def help(arr, l, r):
            
            if l==r:
                return l
            mid=(r+l)//2
            if arr[mid]>arr[mid+1]:
                return help(arr, l, mid)
            return help(arr, mid+1, r)
        
        return help(nums, 0, len(nums)-1)
                