class Solution:
    def countSegments(self, s: str) -> int:
#         if len(s)==0:
#             return 0
#         s+=' '
#         s=list(s)
        
#         temp=[]
#         res=[]
        
#         for i in range(len(s)):
#             if s[i]!=' ' and i<len(s)-1:
#                     temp.append(s[i])
                
#             else:
#                 res.append(temp)
#                 temp=[]
#         final=[]       
#         for word in res:
#             final.append(''.join(word))
            
#         return len(final)
          
        s+=' '
        prev=' '
        count=0
        for ele in s:
            if prev!=' ' and ele==' ':
                count+=1
                prev=' '
            else:
                prev=ele
                
        return count
                