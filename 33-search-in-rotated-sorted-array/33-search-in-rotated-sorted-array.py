class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if len(nums) == 1 and nums[0] == target:
            return 0
        elif len(nums) == 1 and nums[0] != target:
            return -1
        
        l = 0
        h = len(nums) - 1
        
        while l <= h:
            mid = (l + h) // 2
            
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[l]: # left array sorted
                if nums[l] <= target and target < nums[mid]:
                    h = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[h] >= target and target > nums[mid]:
                    l = mid + 1
                else:
                    h = mid - 1
        return -1