class Solution:
    def sortArrayByParity(self, arr: List[int]) -> List[int]:
        e = []
        o = []
        
        for i in arr:
            if i % 2 == 0:
                e.append(i)
            else:
                o.append(i)
        return e + o
                
        