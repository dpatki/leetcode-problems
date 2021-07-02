#submitted 01/07/2021
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        try:
            tortise = head.next
            hare = head.next.next
        except:
            return None
        
        while tortise != hare:
            try:
                tortise = tortise.next
                hare = hare.next.next
            except:
                return None
        
        counter = 0
        tortise = head
        while tortise != hare:
            tortise = tortise.next
            hare = hare.next
            counter += 1
        
        final = head
        for i in range(counter):
            final = final.next
        
        return final
            