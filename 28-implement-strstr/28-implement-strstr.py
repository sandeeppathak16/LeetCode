class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        
#         n=len(haystack)
#         m=len(needle)
        
#         if m==0:
#             return 0
#         i=0
#         j=0
#         res=-1
#         while i<n and n-i+1>=m:
#             if haystack[i]==needle[j]:
#                 res=i
#                 while j<m and i<n and haystack[i]==needle[j]:
#                     i+=1
#                     j+=1
#                 if j==m:
#                     return res
#                 i=res+1
                
#                 res= -1
                
#                 j=0
#             else:
#                 i+=1
                
#         return res
        if needle == "":
            return 0
        else:
            i=0
            j=len(needle)-1
            while j<len(haystack):
                l=0
                n=len(needle)-1
                if(haystack[i]==needle[l] and haystack[j]==needle[n]):
                    for k in range(i,j+1):
                        if needle[l]==haystack[k]:
                            l+=1
                        else:
                            break
                if (l==len(needle)):
                    return i
                i+=1
                j+=1
            return -1
                


            
                    
            