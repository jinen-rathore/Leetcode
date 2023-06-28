class Solution:
    def countBits(self, n: int) -> List[int]:
        l = []
        for i in range(n+1):
            b = str(bin(i))
            l.append(b.count('1'))
        return l