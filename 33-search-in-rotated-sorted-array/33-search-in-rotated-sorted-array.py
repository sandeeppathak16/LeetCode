class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums)-1
        pivot = 0
        
        def Bsearch(l, left, right, t):
            
            while left<=right:
                mid = (left+right)//2
                
                if l[mid]==t:
                    return mid
                elif l[mid]>t:
                    right = mid-1
                else:
                    left=mid+1
            return -1
        
        if nums[i]>nums[j]:
            pivot = nums.index(max(nums))
            a1 = Bsearch(nums, 0, pivot, target)
            a2 = Bsearch(nums, pivot+1, j, target)
            if a1!= -1:
                return a1
            elif a2!= -1:
                return a2
            else:
                return -1
        else:
            return Bsearch(nums, i, j, target)
            
                    