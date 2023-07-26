class Solution:
    def hammingWeight(self, n: int) -> int:
        b = bin(n)[2:]
        
        count = 0
        
        for i in b:
            if i == "1":
                count += 1
        return count