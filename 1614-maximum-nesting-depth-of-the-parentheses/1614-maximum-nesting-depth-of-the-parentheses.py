class Solution:
    def maxDepth(self, s: str) -> int:
        open_phar = 0
        depth = 0
        
        for i in s:
            if i == "(":
                open_phar += 1
                depth = max(depth, open_phar)
            if i == ")":
                open_phar -= 1
        return depth
                
        