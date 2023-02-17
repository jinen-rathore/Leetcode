class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        
        while r - l > 1:
            mid = (r+l)//2
            
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        if nums[l] == target:
            return l
        elif nums[r] == target:
            return r
        else:
            return -1