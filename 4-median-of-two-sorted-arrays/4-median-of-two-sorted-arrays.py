class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num = nums1 + nums2
        num=sorted(num)
        l = len(num)
        
        if l%2==0:
            m = (float(num[l//2]) + float(num[l//2 - 1]))/2
            return m
        else:
            return float(num[l//2])
            