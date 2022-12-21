class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        l = sorted(nums)
        print(l)
        for i in range(n):
            if l[i] - i != 0:
                return i
        return n
        