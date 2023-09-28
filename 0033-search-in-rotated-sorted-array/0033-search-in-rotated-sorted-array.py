class Solution:
    def search(self, arr: List[int], target: int) -> int:
        
        # optimal solution using binary search
        
        l, h = 0, len(arr) - 1
        
        while l <= h:
            mid = (l + h) // 2
            # base case
            if arr[mid] == target:
                return mid

            # finding the sorted half
            # to find the left sorted half the condition is arr[mid] >= arr[left]
            if arr[l] <= arr[mid]: # left half sorted
                # checking for the target lies between low and mid
                if arr[l] <= target and target <= arr[mid]:
                    h = mid - 1
                else:
                    l = mid + 1
            else: # right half sorted
                if arr[mid] <= target and target <= arr[h]:
                    l = mid + 1
                else:
                    h = mid - 1
        return -1
                
        
#         if len(nums) == 1 and nums[0] == target:
#             return 0
#         elif len(nums) == 1 and nums[0] != target:
#             return -1
        
#         l = 0
#         h = len(nums) - 1
        
#         while l <= h:
#             mid = (l + h) // 2
            
#             if nums[mid] == target:
#                 return mid
#             if nums[mid] >= nums[l]: # left array sorted
#                 if nums[l] <= target and target < nums[mid]:
#                     h = mid - 1
#                 else:
#                     l = mid + 1
#             else: #right part sorted
#                 if nums[h] >= target and target > nums[mid]:
#                     l = mid + 1
#                 else:
#                     h = mid - 1
#         return -1