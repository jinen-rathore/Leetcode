class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        max_num = -1
        
        for num in nums:
            if num > 0:
                if -1*num in nums:
                    max_num = max(max_num, num)
        return max_num