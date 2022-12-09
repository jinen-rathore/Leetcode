class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checker = {}
        for i, v in enumerate(nums):
            if target - v in checker:
                return [checker[target - v], i]
            else:    
                checker[v] = i
        return []        