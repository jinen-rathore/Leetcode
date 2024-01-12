class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        arr = []
        for x,y in points:
            arr.append(x)
            
        arr.sort()
        
        max_diff = 0
        for i in range(len(arr)-1):
            max_diff = max(max_diff, arr[i+1]-arr[i])
        return max_diff
            