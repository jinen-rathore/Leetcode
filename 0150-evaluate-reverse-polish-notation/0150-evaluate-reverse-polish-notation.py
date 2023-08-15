class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        for ele in tokens:
            if ele not in '+-*/':
                stack.append(int(ele))
            else:
                n1 = stack.pop()
                n2 = stack.pop()
                if ele == "+":
                    stack.append(n1 + n2)
                
                elif ele == "-":
                    stack.append(n2 - n1)
                
                elif ele == "*":
                    stack.append(n1 * n2)
                
                else:
                    stack.append(int(n2/n1))
                    
        return stack.pop()