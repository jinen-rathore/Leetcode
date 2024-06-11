class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d = {}
        res = []
        
        for i in arr1:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
                
        for i in arr2:
            res.extend([i] * d[i])
            del d[i]
        for i in sorted(d.keys()):
            res.extend([i] * d[i])
        
        return res