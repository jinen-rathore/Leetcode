class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        d = {}
        for val in nums:
            if val in d:
                d[val] += 1
            else:
                d[val] = 1
        for key in d:
            if d[key] == 1:
                return key