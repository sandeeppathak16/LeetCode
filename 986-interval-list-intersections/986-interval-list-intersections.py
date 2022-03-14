class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        res=[]
        while firstList and secondList:
            x1, x2=firstList[0]
            y1, y2=secondList[0]
            
            if x2<y1:
                firstList.pop(0)
            elif y2<x1:
                secondList.pop(0)
            else:
                res.append([max(x1, y1), min(x2, y2)])
                if x2<y2:
                    firstList.pop(0)
                else:
                    secondList.pop(0) 
        return res