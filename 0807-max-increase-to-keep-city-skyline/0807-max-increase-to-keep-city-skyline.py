class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        # the logic is we need to find the min of the two max elements 
        # present in the row and col of that index
        
        # ex for gird[0][0] = 3
        # we will see 0th row and find max element in 0th row
        # then we will see 0th col and find the max elements in the 0th col
        # then we will assign min(max row element, max col element) in the grid[0][0]
        # then continue soo on
        
        total_cost = 0
        
        row_max = [max(row) for row in grid]
        transposed = zip(*grid)
        col_max = [max(col) for col in transposed]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                total_cost += min(row_max[i], col_max[j]) - grid[i][j]
                
        return total_cost
            
        