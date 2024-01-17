class Solution:
    def minOperations(self, n: int) -> int:
        arr = [2*x+1 for x in range(n)]
        target = sum(arr) // n
        
        operations = 0
        
        for i in range(len(arr)//2):
            operations += target - arr[i]
        return operations