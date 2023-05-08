class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        open_ = 0
        close_ = 0
        
        res = ""
        
        start = 0
        
        for i, c in enumerate(s):
            if c == "(":
                open_ += 1
            elif c == ")":
                close_ += 1
                
            if open_ == close_:
                res += s[start+1: i]
                start = i + 1
        return res
                