# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        q = None
        r = None
        
        while p:
            r = q
            q = p
            p = p.next
            
            q.next = r
        head = q
        return q
        
        # Time complexity = O(N)
        
#         prev = None
#         curr = head
        
#         while curr:
#             temp = curr.next
#             curr.next = prev
#             prev = curr
#             curr = temp
#         return prev
            