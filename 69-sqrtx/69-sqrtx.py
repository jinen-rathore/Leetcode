class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        l,r = 0,x
        while l <= r:
            mid = (l+r) // 2
            
            if mid*mid <= x < (mid+1)*(mid+1):
                return mid
            elif x < mid*mid:
                r = mid
            else:
                l = mid