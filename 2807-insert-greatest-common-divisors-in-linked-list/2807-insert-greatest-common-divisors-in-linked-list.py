# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Finding GCD 
        def findGCD(a,b):
            if b == 0:
                return a
            return findGCD(b, a%b)
        
        curr = head
        # creating a node and inserting in a linked list as usual
        while curr and curr.next:
            curr.next = ListNode(findGCD(curr.val, curr.next.val), next = curr.next)
            curr = curr.next.next
        return head
            
            
            
            