# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
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
        