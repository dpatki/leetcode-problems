#submitted 14/02/2022
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        h = []
        for i in range(len(lists)):
            elem = lists[i]
            if elem:
                heappush(h, (elem.val, i, elem))
        if not h:
            return None
        head = ListNode()
        cur = head
        while h:
            thing = heappop(h)
            cur.val = thing[0]
            if thing[2].next:
                thing = (thing[2].next.val, thing[1], thing[2].next)
                heappush(h, thing)
            nexty = ListNode()
            if h:
                cur.next = nexty 
            cur = nexty 
        return head
             