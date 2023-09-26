class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        
        # row = [0] * n => matrix[i][..]
        # col = [0] * m => matrix[..][j]
        # for the first element we take col0 variable
        
        col0 = 1
        
        # instead of taking extra lists we consider the 1st row and 1st col as out reference
        # since the postion 0,0 overlaps we take 1st column full but for the row we take from 2nd element to all
        # for that position we take a variable col0 to store it
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    # we mark the ith row in col0 and jth col in row0
                    matrix[i][0] = 0
                    # if it is not the 0,0 element we mark in the col else in the col0 variable
                    if j != 0:
                        matrix[0][j] = 0
                    else:
                        col0 = 0
        # we iterate from the 2nd row and 2nd column
        # we are not touching the 1st row and col for now
        # just iterating and checking if the marked row or col is equal to 0 then we mark that place as 0
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # step 3 we are checking if the 0,0 element is 0 or not 
        # if it is 0 then we first change the col to 0
        if matrix[0][0] == 0:
            for j in range(m): matrix[0][j] = 0
        
        # similarly if the col0 value is 0 
        # then only we set the first row as 0
        if col0 == 0:
            for i in range(n): matrix[i][0] = 0
        