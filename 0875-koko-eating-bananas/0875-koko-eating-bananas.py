import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # for the optimal approach we will be using binary search
        
        # we go from 1 to the max values in the plies list
        low, high = 1, max(piles)
        while low <= high:
            # calculating mid value
            mid = (low + high) // 2
            
            # so we need to find the total number of hours koko takes to eat all the bananas
            # we can get that by dividing each vales of the piles list by the mid value
            # then adding them up
            req_hours = 0
            for i in range(len(piles)):
                req_hours += math.ceil(piles[i] / mid)
            
            # if the hours is less than or equal to h:
            # h is a candidate and we can find h so we eliminate the right part of the numbers
            if req_hours <= h:
                high = mid - 1
            # else we eliminate the left part of numbers
            else:
                low = mid + 1
        return low
        