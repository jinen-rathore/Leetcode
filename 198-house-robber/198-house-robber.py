class Solution:
    def rob(self, nums: List[int]) -> int:
        curr = prev = 0
        for i in nums:
            prev, curr = curr, max(i + prev, curr)
        return curr