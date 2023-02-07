class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # method 1
#         left, right = 0, len(matrix) - 1
        
#         while left < right:
#             for i in range(right - left):
#                 top, bottom = left, right 
                
#                 topLeft = matrix[top][left+i]
            
#                 matrix[top][left+i] = matrix[bottom-i][left]
            
#                 matrix[bottom-i][left] = matrix[bottom][right-i]
            
#                 matrix[bottom][right-i] = matrix[top+i][right]
            
#                 matrix[top+i][right] = topLeft
                
#             left += 1
#             right -= 1

        # Method 2
        left = 0
        right = len(matrix) - 1
        
        # revers the matrix
        while left < right:
            matrix[left], matrix[right] = matrix[right], matrix[left]
            right -= 1
            left += 1
            
        # transpose the matrix
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
                