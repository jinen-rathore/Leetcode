class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        """# Brute Force solution
        for i in range(len(arr)-2):
            if arr[i] % 2 == 1 and arr[1+1] % 2 == 1 and arr[i+2] % 2 == 1:
                return True
        return False"""
        
        # using counting
        
        odd_count = 0
        for i in range(len(arr)):
            if arr[i] % 2 == 1:
                odd_count += 1
            else:
                odd_count = 0
            if odd_count == 3:
                return True
        return False