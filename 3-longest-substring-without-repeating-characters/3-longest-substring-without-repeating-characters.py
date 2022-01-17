class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l =[]
        max_l =[]
        i=0
        if len(s)==1:
            return 1
        
        while i<len(s):
            for letter in s[i:]:
                if letter not in l:
                    l.append(letter)
                else:
                    max_l.append(len(l))
                    l.clear()
                    break
            i+=1
        if len(max_l)==0:
            max_v = len(l)
        else:
            max_v =max(max_l)
        return max_v