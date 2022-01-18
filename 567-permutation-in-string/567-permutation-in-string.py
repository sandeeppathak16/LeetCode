class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        r = 0
        l = r+len(s1)
        print(s2[r:l])

        while l <= len(s2):
            s22 = list(s2[r:l])
            for char in s1:
                if char not in s22:
                    r +=1
                    l +=1
                else:
                    s22.remove(char)
                if len(s22) == 0:
                    return True
        return False