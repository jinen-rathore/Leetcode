# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """        
        # Iterative Method
        
        # we use 3 pointers
        # at the start both previous and next are none
        p,n = None, None
        # and current is at head
        c = head
        
        # we traverse till current is null
        while c:
            
            # we first store the next value after current
            n = c.next
            # then we break the link from and reverse it
            # basically pointing current's next to previous reverses the link
            c.next = p
            # then we move 
            # first previous is moved to current 
            p = c
            # then current is moved to next
            c = n
        # at the end when current is Null the previous is at the last node so we return that
        return p
        """
        
        # Recursive Method
        def recursiveReverseList(self, node, p = None):
            # similarly to the iterative solution we will use the same concept
            # we return previous when current is Null
            if not node:
                return p
            
            # else we store the next 
            n = node.next
            # move the next to current to previous
            node.next = p
            # then we move the previous to current
            p = node
            # to get move the current to next node we use recursion
            return recursiveReverseList(self, n, node)
        return recursiveReverseList(self, head)