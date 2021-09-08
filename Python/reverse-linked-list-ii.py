#submitted 29/08/2021

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def reverseList(node):
            prev = None
            while node:
                curr = node
                node = node.next
                curr.next = prev
                prev = curr
            return prev
        
        if left == right:
            return head
        if left == 1:
            etracker = head
            for i in range(1, right):
                etracker = etracker.next
            last = etracker.next
            etracker.next = None
            
            res = reverseList(head)
            temp = res
            while temp.next:
                temp = temp.next
            temp.next = last
            return res
                
        
        stracker = head
        for i in range(1, left - 1):
            stracker = stracker.next
        
        etracker = head
        for i in range(1, right):
            etracker = etracker.next
        
        last = etracker.next
        etracker.next = None
        
        res = reverseList(stracker.next)
        stracker.next = res
        while res.next:
            res = res.next
        
        res.next = last
        
        return head
        