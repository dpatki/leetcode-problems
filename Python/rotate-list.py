#submitted 12/02/2022

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        start = head
        size = 1
        while start.next:
            start = start.next
            size += 1
        offset = k % size
        if offset == 0:
            return head
        start.next = head
        for i in range(size-offset):
            start = start.next
        
        thing = start.next
        start.next = None
        return thing