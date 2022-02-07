class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        res =[]
        for i in range(len(candies)):
            max_c = candies[i]+extraCandies
            res.append(max_c >= max(candies))
        return res
                