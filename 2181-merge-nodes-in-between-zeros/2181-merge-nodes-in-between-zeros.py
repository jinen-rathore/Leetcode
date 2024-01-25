# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        cur = head.next
        curr_sum = 0
        while cur:
            if cur.val == 0:
                prev = prev.next
                prev.val = curr_sum
                curr_sum = 0
            else:
                curr_sum += cur.val
            cur = cur.next
        prev.next = None
        return head.next
                