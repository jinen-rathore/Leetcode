class Solution:
    def decodeString(self, s: str) -> str:
        # we will be using a stack to store the elements
        stack = []
        
        # looping through the characters 
        for char in s:
            
            # appending everything to the stack except the closing bracket "]"
            if char != "]":
                stack.append(char)
            
            # if there is a closing bracket then there are 2 case
            else:
                
                # case 1 we first need to pop out the substring 
                substring = ""
                
                # we are checking till the stack top is open bracket "["
                while stack[-1] != "[":
                    
                    # appending the substring 
                    substring = stack.pop() + substring
                
                # we pop out the open bracket to get the numbers
                stack.pop()
                
                # case 2: taking out the numbers 
                num = ""
                
                # we will be poping till the stack is not empty and the top of the stack is a digit
                while stack and stack[-1].isdigit():
                    
                    # adding it to the num string
                    num = stack.pop() + num
                
                # we will be appending the substring to the stack again by multiplying the number
                stack.append(int(num) * substring)
                
        return "".join(stack)