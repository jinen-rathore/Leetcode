import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # for the optimal approach we will be using binary search
        low, high = 1, max(piles)
        while low <= high:
            mid = (low + high) // 2
            
            req_hours = 0
            for i in range(len(piles)):
                req_hours += math.ceil(piles[i] / mid)
            
            if req_hours <= h:
                high = mid - 1
            else:
                low = mid + 1
        return low
        