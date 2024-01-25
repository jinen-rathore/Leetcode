# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        def binToDec(n):
            decimal = 0
            power = 1
            
            while n > 0:
                rem = n % 10
                n = n // 10
                decimal += power * rem
                power = power * 2
            return decimal
        
        s = ""
        while head:
            s += str(head.val)
            head = head.next
        return binToDec(int(s))