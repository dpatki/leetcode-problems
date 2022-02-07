#submitted 19/01/2022
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0, None)
        one = l1
        two = l2
        carry = 0
        cur = head
        prev = None
        while one and two:
            summ = (one.val + two.val + carry) % 10
            carry =  (one.val + two.val + carry) // 10
            one = one.next
            two = two.next
            cur.val = summ
            after = ListNode(0, None)
            cur.next = after
            prev = cur
            cur = after
        
        while one:
            summ = (one.val  + carry) % 10
            carry =  (one.val + carry) // 10
            one = one.next
            cur.val = summ
            after = ListNode(0, None)
            cur.next = after
            prev = cur
            cur = after
        
        while two:
            summ = (two.val + carry) % 10
            carry =  (two.val + carry) // 10
            two = two.next
            cur.val = summ
            after = ListNode(0, None)
            cur.next = after
            prev = cur
            cur = after
        
        if carry:
            cur.val = 1
        else:
            prev.next = None
        
        return head