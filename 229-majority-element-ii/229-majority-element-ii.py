class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        l = []
        for key in d:
            if d[key] > (len(nums) // 3):
                l.append(key)
        return l