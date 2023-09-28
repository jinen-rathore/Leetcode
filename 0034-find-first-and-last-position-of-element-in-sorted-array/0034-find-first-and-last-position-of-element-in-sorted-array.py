class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if len(nums) == 0:
            return [-1, -1]
        
        if len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]

        start = 0
        end = len(nums) - 1
        ans = []        
        
        while start <= end:
            
            if nums[start] != target:
                start += 1
            if nums[end] != target:
                end -= 1
            
            if nums[start] == target and nums[end] == target:
                ans.append(start)
                ans.append(end)
                break
            if start > end:
                ans.append(-1)
                ans.append(-1)
        return ans