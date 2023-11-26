class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        critical_num = max(candies) - extraCandies
        res = []
        for n in candies:
            if n < critical_num:
                res.append(False)
            else:
                res.append(True)
        return res