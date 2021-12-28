# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if isBadVersion(0):
            return 0
        
        i, j = 0, n
        while i <= j:
            m = (i + j) // 2
            if isBadVersion(m):
                if not isBadVersion(m-1):
                    return m
                else:
                    j = m  
            else:
                if isBadVersion(m+1):
                    return m+1
                else:
                    i = m +1
        