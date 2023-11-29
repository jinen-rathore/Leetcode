class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r_count = 0
        max_count = 0
        for char in s:
            if char == "R":
                r_count += 1
            if char == "L":
                r_count -= 1
            if r_count == 0:
                max_count += 1
        return max_count
                
                
        