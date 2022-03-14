class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        
        if len(nums1)>len(nums2):
            for ele in nums1:
                count1=nums1.count(ele)
                count2=nums2.count(ele)
                if ele not in res:
                    for  i in range(min(count1, count2)):
                        res.append(ele)
        else:
            for ele in nums2:
                count1=nums1.count(ele)
                count2=nums2.count(ele)
                if ele not in res:
                    for  i in range(min(count1, count2)):
                        res.append(ele)
                    
        return res