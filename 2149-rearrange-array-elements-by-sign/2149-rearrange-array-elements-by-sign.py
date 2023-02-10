class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p = []
        n = []
        
        res = []
        
        for i in nums:
            if i > 0:
                p.append(i)
            else:
                n.append(i)
        i = 0
        j = 0
        while i < len(p) or j < len(n):
            res.append(p[i])
            res.append(n[j])
            i += 1
            j += 1
        return res