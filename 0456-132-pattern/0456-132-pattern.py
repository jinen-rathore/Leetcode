class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        #brute force solution
        """
        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                for k in range(j,n):
                    if nums[i] < nums[k] < nums[j]:
                        return True
        return False
        """
        
        #Optimal Solution using monotonic decresing stack
        
        stack = [] # this takes a pair(number, minimum before that number)
        currMin = nums[0]
        
        # we iterate thourgh the nums array from 1 because the 1st value can only be i 
        # as nums[i] < nums[k] < nums[j]
        for n in nums[1:]: 
        
            # till our stack is empty or the new number > the top of stack:
            # we pop all the elements because it is a mono dec stack
            # here stack[-1] gets me to the last element and stack[-1][0] gets the number
            while stack and stack[-1][0] <= n:
                stack.pop()
            
            # if the stack is not empty and
            # the stack top is greater than the new number
            # and the minimun is less than the number
            # we found the pair
            # as it satisfys the condition nums[i] < nums[k] < nums[j]
            # where nums[i] is the currMin, nums[j] is the incoming number (n)
            # and nums[k] is the stack top or the max value 
            if stack and n > stack[-1][1]:
                return True
            
            # else we append the number and minimum to the stack
            stack.append([n, currMin])
            currMin = min(currMin, n)
        return False
        