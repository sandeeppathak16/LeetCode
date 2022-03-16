class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # check={}
        # if len(s)!=len(t):
        #     return False
        # for i in range(len(s)):
        #     if s[i] not in check:
        #         if t[i] not in check.values():
        #             check[s[i]]=t[i]
        #         else:
        #             False
        #     else:
        #         if check[s[i]]!=t[i]:
        #             return False
        # return True
        
        d = {}
        for i in range(len(s)):
            if s[i] not in d:
                if t[i] not in d.values():
                    d[s[i]] = t[i]
                else:
                    return False
            else:
                if d[s[i]] != t[i]:
                    return False
        return True
                