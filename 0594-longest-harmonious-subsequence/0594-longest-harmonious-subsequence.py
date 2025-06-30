class Solution:
    def findLHS(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        max_count = 0
        for key, val in d.items():
            if key + 1 in d:
                max_count = max(max_count, d[key] + d[key+1])
        return max_count