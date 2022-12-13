# Time complexity: O(N^2)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sorting the numbers 
        nums.sort()
        result = [] 
        
        # checking if the next number in nums is similar to the previous number ex: nums[0] == nums[1] if it is there continue 
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue

            # else do the 2 sum problem for the remaining elements in nums
            # creating 2 pointers l at the start of the elements and r at the end of the elements
            l, r = i + 1, len(nums) - 1
            # run till l < r 
            while l < r:
                # caclulating the sum using the condition given in question
                threeSum = nums[l] + nums[r] + a
                # if the sum is greater than 0 then decrement the right pointer as it will decrease the sum because the list is sorted
                if threeSum > 0:
                    r -= 1
                # if the sum is les than 0 then increment the left pointer
                elif threeSum < 0:
                    l += 1
                # if the sum is 0 the append the elements to the list
                else:
                    result.append([a,nums[l],nums[r]])
                    # append the pointer once
                    l +=1
                    # if there is a similar element after incremeting then increment till it becomes different as it will give the same results 
                    while nums[l] == nums[l - 1] and l < r:
                        l +=1
        return result
                
        
        
            