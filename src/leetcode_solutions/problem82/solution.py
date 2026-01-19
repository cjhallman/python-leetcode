from typing import Optional

from leetcode_solutions.nodes.nodes import ListNode


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Keep track of start with start.next = head
        l pointer starts at start
        r starts at head
        while r is not None:
            if r.val == r.next.val -> r = r.next
            else: l.next = r
                l = l.next
                r = r.next
        STOP once you reach the end of the list
        """
        if not head or not head.next:
            return head
        start = ListNode(0, head)
        p1, p2, p3 = start, head, head.next
        while p3:
            print(f"Looking at p1: {p1.val}, p2: {p2.val}, p3: {p3.val}")
            if p2.val == p3.val:
                while p3 and p2.val == p3.val:
                    p3 = p3.next
                p1.next = p3
                p2 = p3
                p3 = p2.next if p2 else None
            else:
                p1 = p2
                p2 = p3
                p3 = p3.next
        return start.next
