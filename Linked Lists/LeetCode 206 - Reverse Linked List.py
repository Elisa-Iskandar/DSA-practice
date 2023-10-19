class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        output = None
        current = head
        while current:
            next_node = current.next
            current.next = output
            output = current
            current = next_node
        return output
