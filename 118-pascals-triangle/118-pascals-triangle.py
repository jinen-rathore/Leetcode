class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        else:
            r = [[1],[1,1]]
            output = [1,1]
            for i in range(numRows-2):
                new = []
                for i in range(len(output)-1):
                    left = output[i]
                    right = output[i+1]
                    new.append(left + right)
                new = [1] + new + [1]
                output = new
                r.append(output)
            return(r)