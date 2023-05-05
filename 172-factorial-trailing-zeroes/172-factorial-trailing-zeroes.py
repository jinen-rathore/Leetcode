class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n > 4:
            count += int(n/5)
            n = int(n/5)
        return count