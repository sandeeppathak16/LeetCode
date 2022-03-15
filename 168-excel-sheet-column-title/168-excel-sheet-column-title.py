class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ""
        
        while columnNumber:
            columnNumber, r = (columnNumber-1)//26, (columnNumber-1)%26
            ans = chr(ord("A")+r) + ans
        
        return ans