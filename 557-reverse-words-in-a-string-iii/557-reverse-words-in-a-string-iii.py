class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split(" ")
        i = 0
        str1= " "
        for ele in l:
            l[i]= ele[::-1]
            i+=1
        return (str1.join(l))