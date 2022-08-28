# Definition for singly-linked list.
#class ListNode:
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        result = ListNode(0, None)
        pointer = result
        carry = 0
        
        while l1 or l2:
            digit1, digit2 = 0, 0
            if l1:
                digit1 = l1.val
                l1 = l1.next
            if l2:
                digit2 = l2.val
                l2 = l2.next
        
            sums = digit1 + digit2 + carry
            carry, remainder = divmod(sums,10)
            pointer.next = ListNode(remainder, None)
            pointer = pointer.next
        
        if carry ==1:
            pointer.next = ListNode(1, None)
        
        return result.next