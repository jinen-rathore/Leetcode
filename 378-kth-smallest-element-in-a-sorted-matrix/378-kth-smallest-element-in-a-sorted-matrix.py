class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l = []
        while matrix:
            l.extend(matrix.pop(0))
        l.sort()
        return l[k-1]