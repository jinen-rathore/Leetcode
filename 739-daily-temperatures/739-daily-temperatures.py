class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackValue, stackIndex  = stack.pop()
                result[stackIndex] = (i - stackIndex)
            stack.append([temp, i])
            
        return result