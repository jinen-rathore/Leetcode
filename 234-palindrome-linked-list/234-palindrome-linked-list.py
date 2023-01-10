# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # method 1
        # put the linked list into array and solve the problem
#         arr = []
        
#         while head:
#             arr.append(head.val)
#             head = head.next
        
#         l,r = 0, len(arr) - 1
#         while l <= r:
#             if arr[l] != arr[r]:
#                 return False
#         return True
        # return arr == arr[::-1]
        
#         Method 2
        
        #finding mid point
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        #reversing the second half
        
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
