class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        from itertools import combinations
        
        l = []
        
        for i in range(1, n+1):
            l.append(i)
        comb = combinations(l, k)
        return comb