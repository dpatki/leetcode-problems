#submitted 22/01/2022

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tortise = head
        hare = head.next
        while(hare):
            tortise = tortise.next
            
            hare = hare.next
            if hare:
                hare = hare.next
        
        return tortise