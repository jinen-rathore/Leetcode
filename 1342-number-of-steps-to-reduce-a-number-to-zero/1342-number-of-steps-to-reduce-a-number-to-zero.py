class Solution:
    def numberOfSteps(self, num: int) -> int:
        # bit counting 
        # counting the number of 0 and 1 in binary
        steps = num == 0
        while num > 0:
            steps += 1 + (num & 1)
            num >>= 1
        return steps - 1