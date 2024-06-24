class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
        # 2,4,1,2,7,8
        # 1,2,2,4,7,8
        
        # 9,8,7,6,5,1,2,3,4
        # 1,2,3,4,5,6,7,8,9
        # (9,8,1),(7,6,2),(5,4,3) = 8+6+4
        
        piles.sort()
        
        rem = len(piles)//3
        piles = piles[rem:]
        cost, i = 0, 0
        while i < len(piles):
            cost += piles[i]
            i += 2
        return cost