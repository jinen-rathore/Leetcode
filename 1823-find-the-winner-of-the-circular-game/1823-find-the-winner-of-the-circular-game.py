class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [x+1 for x in range(n)]
        m = 0
        
        while len(arr) > 1:
            m = (m + k - 1) % len(arr)
            arr.pop(m)
        return arr[0]
            
            