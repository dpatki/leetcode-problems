#submitted 18/08/2022

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return list1
        if not list1:
            return list2
        if not list2:
            return list1
        heady = None
        if list1.val < list2.val:
            heady = list1
            list1 = list1.next
        else:
            heady = list2
            list2 = list2.next
        cur = heady
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        if not list1 and list2:
            cur.next = list2
        if not list2 and list1:
            cur.next = list1
        return heady