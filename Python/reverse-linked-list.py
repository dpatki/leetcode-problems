#submitted 29/08/2021

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    first = None
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        def helper(node):
            if node.next == None:
                self.first = node
                return node
            res = helper(node.next)
            res.next = node
            return node
        if not head.next:
            return head
        second = helper(head.next)
        second.next = head
        head.next = None
        return self.first