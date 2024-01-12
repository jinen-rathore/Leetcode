class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        def ds(n):
            digit_sum = 0
            while n:
                digit_sum += n%10
                n = n // 10
            return digit_sum
                
                
        ele_sum = 0
        digit_sum = 0
        
        for num in nums:
            ele_sum += num
            digit_sum += ds(num)
        return ele_sum - digit_sum
            