class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        # Assigning the result to max of the numbers
        # for ex if arr is [-1] then the max is -1 
        res = max(nums)
        
        # the current max and current min to 1
        currMax, currMin = 1, 1
        
        for i in nums:
            
            # contiue if i is equal to 0 as it resests the currMax and currMin so check before
            if i == 0:
                currMax, currMin = 1,1
                continue
                
            # this temp is to check the current max values before assigment of current max as we need to find min in currentMin using the value of currMax before assignment
            temp = i * currMax
            # current max is max of number*currentmax, number*currentmin and the number itself ex [-1, 8] => 8
            currMax = max(i * currMax, i * currMin, i)
            # current min is mim of number*currentmax, number*currentmin and the number itself ex [-1, -8] => -8
            currMin = min(temp, i * currMin, i)

            res = max(res, currMax)
                
        return res