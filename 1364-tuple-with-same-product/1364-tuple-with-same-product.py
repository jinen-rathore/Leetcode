class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        d = {}
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                p = nums[i] * nums[j]
                if p in d:
                    d[p] += 1
                else:
                    d[p] = 1
        res = 0
        print(d)
        for val in d.values():
            if val > 1:
                res += val * (val-1) * 4
        return res