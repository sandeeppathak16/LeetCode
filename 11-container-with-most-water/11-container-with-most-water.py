class Solution:
    def maxArea(self, height: List[int]) -> int:
        area=0
        i=0
        j=len(height)-1

        while i<j:
            minh=min(height[i],height[j])
            ar=minh*(j-i)
            area=max(area,ar)

            if height[i]>height[j]:
                j-=1
            else:
                i+=1
        return area
                    
                