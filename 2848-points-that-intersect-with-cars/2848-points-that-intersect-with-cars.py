class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        # h = [0] * 101
        # for s,e in nums:
        #     for i in range(s, e+1):
        #         h[i] = 1
        # count = 0
        # for i in h:
        #     if i == 1:
        #         count += 1
        # return count
        
        se = set()
        for s,e in nums:
            for i in range(s,e+1):
                se.add(i)
        return len(se)
                