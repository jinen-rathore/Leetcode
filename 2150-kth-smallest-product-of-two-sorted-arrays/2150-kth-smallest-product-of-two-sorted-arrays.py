import bisect
import math
class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def countLessEqual(x):
            count = 0
            for a in nums1:
                if a > 0:
                    count += bisect.bisect_right(nums2, x // a)
                elif a < 0:
                    count += len(nums2) - bisect.bisect_left(nums2, math.ceil(x / a))
                else:  # a == 0
                    if x >= 0:
                        count += len(nums2)
            return count

        low, high = -10**10, 10**10
        while low < high:
            mid = (low + high) // 2
            if countLessEqual(mid) < k:
                low = mid + 1
            else:
                high = mid
        return low
