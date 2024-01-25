# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # we take 2 pointers
        # previous that will point to the first zero
        # current that will calculate sum and will encounter the second zero
        prev = head
        cur = head.next
        curr_sum = 0
        while cur:
            # if we ecounter zero
            # we move previous one position 
            # and store the sum there
            if cur.val == 0:
                prev = prev.next
                prev.val = curr_sum
                curr_sum = 0
            # else we just add the sum
            else:
                curr_sum += cur.val
            # we move current evertime
            cur = cur.next
        # since in the end previous will be pointing to the last zero we set its next to none
        prev.next = None
        # similarly to start with the merged node we return next of head
        return head.next
                