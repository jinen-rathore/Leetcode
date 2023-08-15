class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # using backtracking approach
        
        # we can add a open parenthesis if openP count < n
        # we can add a close parhenthsis if openP count > closeP count
        # we stop when openP == closeP == n
        
        stack = []
        res = []
        
        def backtrack(openP, closeP):
            
            if openP == closeP == n:
                res.append("".join(stack))
                return 
            
            if openP < n:
                stack.append("(")
                backtrack(openP + 1, closeP)
                stack.pop()
                
            if closeP < openP:
                stack.append(")")
                backtrack(openP, closeP + 1)
                stack.pop()
                
        backtrack(0, 0)
        return res