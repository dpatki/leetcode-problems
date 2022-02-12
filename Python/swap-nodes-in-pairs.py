#submitted 12/02/2022

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        prev = None
        first = head
        second = head.next
        start = second
        if not second:
            return first
        while first and second:
            print(first.val, second.val)
            first.next = second.next
            second.next = first
            
            if prev:
                prev.next = second 
            prev = first
            first = first.next
            if first:
                second = first.next
            
           
        return start