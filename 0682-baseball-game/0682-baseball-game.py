class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for char in operations:
            if char == "C":
                stack.pop(-1)
            elif char == "+":
                stack.append(stack[-1] + stack[-2])
            elif char == "D":
                stack.append(2 * stack[-1])
            else:
                stack.append(int(char))
        print(stack)
        return sum(stack)