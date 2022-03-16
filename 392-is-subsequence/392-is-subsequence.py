class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if len(s)>len(t):
            return False
        if s=='':
            return True;
        sub=0
        
        for i in range(len(t)):
            if sub<=len(s)-1:
                if s[sub]== t[i]:
                    sub+=1
                    
        return sub==len(s)

#         if len(s) > len(t):return False
#         if len(s) == 0:return True
#         subsequence=0
#         for i in range(0,len(t)):
#             if subsequence <= len(s) -1:
#                 print(s[subsequence])
#                 if s[subsequence]==t[i]:

#                     subsequence+=1
#         return  subsequence == len(s) 