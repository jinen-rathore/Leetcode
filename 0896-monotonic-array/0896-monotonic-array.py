class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 2:
            return True
        
        inc, dec = False, False
        
        for i in range(1, n):
            if nums[i-1] > nums[i]:
                inc = True
            elif nums[i-1] < nums[i]:
                dec = True
        
        if inc and dec:
            return False
        return True
        