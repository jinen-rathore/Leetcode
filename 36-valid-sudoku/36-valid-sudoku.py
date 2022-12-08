class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        l = []
        for i, row in enumerate(board):
            for j, ele in enumerate(row):
                if ele != ".":
                    l += [(ele,j),(i,ele),(i//3,j//3,ele)]
        return len(set(l)) == len(l)
        
                