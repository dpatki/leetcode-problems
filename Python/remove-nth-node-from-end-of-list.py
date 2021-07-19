#submitted 04/07/2021
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        thing = head
        counter = 0
        while thing:
            thing = thing.next
            counter += 1
        if counter == 1:
            return None
        if counter - n == 0:
            return head.next
        pointer = head
        for i in range(counter - n - 1):
            pointer = pointer.next
        
        pointer.next = pointer.next.next
        
        return head