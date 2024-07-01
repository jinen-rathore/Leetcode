class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(len(arr)-2):
            a,b,c = arr[i], arr[i+1], arr[i+2]
            
            if a % 2 == 1 and b % 2 == 1 and c % 2 == 1:
                return True
        return False