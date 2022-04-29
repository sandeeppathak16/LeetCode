class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(arr, target, first_search):
            l=0
            r=len(arr)-1
            res = -1
            while l<=r:
                mid = l+(r-l)//2
                if arr[mid]==target:
                    res=mid
                    if first_search:
                        r=mid-1
                    else:
                        l=mid+1
                elif arr[mid]<target:
                    l=mid+1
                else:
                    r=mid-1

            return res
        
        res=[search(nums, target, True), search(nums, target, False)]
        
        return res