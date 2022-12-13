# Time complexity: O(N^2)

class Solution:
    
    #approach 1
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
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
    """
        #approach 2

        res = set()

        #1. Split nums into three lists: negative numbers, positive numbers, and zeros
        n = []
        p = []
        z = []
        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0: 
                n.append(num)
            else:
                z.append(num)

        #2. Create a separate set for negatives and positives for O(1) look-up times
        N, P = set(n), set(p)

        #3. If there is at least 1 zero in the list, add all cases where -num exists in N and num exists in P
        #   i.e. (-3, 0, 3) = 0
        if z:
            for num in P:
                if -1*num in N:
                    res.add((-1*num, 0, num))

        #3. If there are at least 3 zeros in the list then also include (0, 0, 0) = 0
        if len(z) >= 3:
            res.add((0,0,0))

        #4. For all pairs of negative numbers (-3, -1), check to see if their complement (4)
        #   exists in the positive number set
        for i in range(len(n)):
            for j in range(i+1,len(n)):
                target = -1*(n[i]+n[j])
                if target in P:
                    res.add(tuple(sorted([n[i],n[j],target])))

        #5. For all pairs of positive numbers (1, 1), check to see if their complement (-2)
        #   exists in the negative number set
        for i in range(len(p)):
            for j in range(i+1,len(p)):
                target = -1*(p[i]+p[j])
                if target in N:
                    res.add(tuple(sorted([p[i],p[j],target])))

        return res



