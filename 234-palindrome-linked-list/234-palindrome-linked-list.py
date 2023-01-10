# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # method 1
        # put the linked list into array and solve the problem
        arr = []
        
        while head:
            arr.append(head.val)
            head = head.next
            
        return arr == arr[::-1]
