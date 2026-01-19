# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        result = []
        node = self
        while node:
            result.append(node.val)
            node = node.next
        return str(result)

    def __str__(self):
        return self.__repr__()

    def __eq__(self, head: ListNode):
        node = self
        while node and head:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return not node and not head


def buildHeadFromList(vals: List[int]):
    if len(vals) == 0:
        return None
    head = ListNode(vals[0])
    node = head
    for i in range(1, len(vals)):
        node.next = ListNode(vals[i])
        node = node.next
    return head
