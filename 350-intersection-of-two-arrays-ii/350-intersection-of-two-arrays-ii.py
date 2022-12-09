class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #if the length of nums2 is greater than nums1 swap the arrays
        if len(nums2) > len(nums1):
            nums1 , nums2 = nums2, nums1
        # create a empyt dictionary to store the frequency values
        s = {}
        # if value of i is not in empyt dictionary then add it as frequency 1
        # else frequency + 1
        for i in nums1:
            if i not in s:
                s[i] = 1
            else:
                s[i] += 1
        # create empyt list for storing results
        l = []
        # for i in nums2 if i is present in sictionay as key and value then append it 
        # to the list decrementing the frequency till frequency becomes 0
        for i in nums2:
            if i in s and s[i]:
                s[i] -= 1
                l.append(i)
        # return list
        return l
