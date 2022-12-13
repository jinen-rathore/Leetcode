class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        nums = list(range(1,n+1))
        for i in range(len(nums)):
            if nums[i] % 15 == 0: 
                nums[i] = "FizzBuzz"
            elif nums[i] % 3 == 0: 
                nums[i] = "Fizz"
            elif nums[i] % 5 == 0: 
                nums[i] = "Buzz"
            else: 
                nums[i] = str(nums[i])
        return nums