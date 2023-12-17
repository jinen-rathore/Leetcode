class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # python one liner
        # return sorted([x**2 for x in nums])
        
        res = [0] * len(nums)
        wrp = len(nums)-1
        p = len(nums)-1
        n = 0
        
        while wrp >= 0:
            if nums[p] ** 2 < nums[n] ** 2:
                res[wrp] = nums[n] ** 2
                wrp -= 1
                n += 1
            else:
                res[wrp] = nums[p] ** 2
                wrp -= 1
                p -= 1
        return res