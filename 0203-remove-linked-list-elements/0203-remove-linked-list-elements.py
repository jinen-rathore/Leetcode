# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return 
        
        head.next = self.removeElements(head.next, val)
        
        return head.next if head and head.val == val else head
#         i = head
#         while i and i.next:
#             if i.next.val == val:
#                 i.next = i.next.next
#             else:
#                 i = i.next
        
#         if head and head.val == val:
#             return head.next
#         else:
#             return head
                
        
        