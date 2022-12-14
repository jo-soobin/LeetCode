class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None
        
        while node:
            # node.next를 이전 prev 리스트로 계속 연결하면서 끝날 때까지 반복
            next, node.next = node.next, prev
            prev, node = node, next
            
        return prev
'''# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        previous = None
        current = head
        next = None

        while (current is not None):
            next = current.next
            current.next = previous
            previous = current
            current = next

        head = previous
        return head'''