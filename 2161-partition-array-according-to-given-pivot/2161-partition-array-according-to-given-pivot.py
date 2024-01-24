class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        s,e,l = [],[],[]
        for i in nums:
            if i < pivot:
                s.append(i)
            elif i == pivot:
                e.append(i)
            else:
                l.append(i)
        return s+e+l