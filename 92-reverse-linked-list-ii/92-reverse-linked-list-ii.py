# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        ReverseList = []
        Pointer = head
        for i in range(right):
            if i - left + 1 >= 0:
                ReverseList.append(Pointer.val)
            Pointer = Pointer.next
        Pointer = head
        for i in range(right):
            if i - left + 1 >= 0:
                Pointer.val = ReverseList.pop()
            Pointer = Pointer.next
        return head