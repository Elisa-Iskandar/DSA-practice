class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev = ListNode(-1)
        prev.next = head
        current = prev
        while current.next != None:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return prev.next
