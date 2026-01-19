from typing import Optional

from leetcode_solutions.nodes.nodes import ListNode


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        """
        l -> Last node < x
        curr -> current_node
        if  curr.val < x:
            temp = l.next
            l.next = curr
            temp_curr = curr.next
            curr.next = temp
            curr = temp_curr
        """
        start = ListNode(0, head)
        left = start
        prev = start
        curr = head
        while curr:
            print(f"l: {left.val}, prev: {prev.val}, curr: {curr.val}")
            if curr.val < x:
                print(f"{curr.val} < {x}")
                if left != prev:
                    print(f"{left.val} != {prev.val}")
                    l_next = left.next
                    left.next = curr
                    print(f"{left.val}.next -> {curr.val}")
                    curr_next = curr.next
                    curr.next = l_next
                    print(f"{curr.val}.next -> {l_next.val}")
                    prev.next = curr_next
                    left = curr
                    curr = curr_next
                else:
                    print(f"{left.val} == {prev.val}")
                    left = curr
                    prev = curr
                    curr = curr.next
            else:
                prev = curr
                curr = curr.next
        return start.next
