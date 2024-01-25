class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        max_len = 1
        curr_len = 1
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                curr_len += 1
                max_len = max(curr_len, max_len)
            else:
                max_len = max(curr_len, max_len)
                curr_len = 1
        return max_len