# submitted 01/08/2021

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        pointer = head
        dicty = {}
        while pointer:
            if pointer.val not in dicty:
                dicty[pointer.val] = 1
            else:
                dicty[pointer.val] += 1
            pointer = pointer.next
        
        pointer = head
        while pointer.next:
            if dicty[pointer.next.val] > 1:
                pointer.next = pointer.next.next
            else:
                pointer = pointer.next
        
        pointer = head
        while pointer:
            if dicty[pointer.val] > 1:
                pointer = pointer.next
            else:
                break
        
        return pointer
                