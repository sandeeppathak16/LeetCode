class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        
        if len(nums1)>len(nums2):
            for ele in nums1:
                if ele in nums2:
                    if ele not in res:
                        res.append(ele)
        else:
            for ele in nums2:
                if ele in nums1:
                    if ele not in res:
                        res.append(ele)
                    
        return res