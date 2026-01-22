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
    
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    """
    Return list representation of binary tree. empty nodes are represented by None
    Example 1: [3, 9, 20, None, None, 15, 7]
            3
           / \
          9  20
            /  \
           15   7
    Example 2: [1, None, 2, 3]
            1
             \
              2
             /
            3
    """
    def __repr__(self):
        result = []
        queue = [self]
        while queue:
            node = queue.pop(0)
            if node:
                result.append(node.val)
                if node.left or node.right:
                    queue.append(node.left)
                    queue.append(node.right)
            else:
                if len(queue) != 0:
                    result.append(None)
        return str(result)
        

    def __str__(self):
        return self.__repr__()

    def __eq__(self, head: TreeNode):
        node = self
        queue = [node]
        head_queue = [head]
        while queue:
            node = queue.pop(0)
            head = head_queue.pop(0)
            if node and head:
                if node.val != head.val:
                    return False
                queue.append(node.left)
                queue.append(node.right)
                head_queue.append(head.left)
                head_queue.append(head.right)
            elif node or head:
                return False
        return True
        

def buildListNodeFromList(vals: List[int]):
    if len(vals) == 0:
        return None
    head = ListNode(vals[0])
    node = head
    for i in range(1, len(vals)):
        node.next = ListNode(vals[i])
        node = node.next
    return head

"""
List should be formatted as 
[head, left, right, left_left, left_right, right_left, right_right, ...]
Example: [3, 9, 20, None, None, 15, 7]
            3
           / \
          9  20
            /  \
           15   7
Example 2: [1, None, 2, 3]
            1
             \
              2
             /
            3
"""
def buildTreeNodeFromList(vals: List[int]):
    if len(vals) == 0:
        return None
    head = TreeNode(vals[0])
    node = head
    queue = [node]
    for i in range(1, len(vals), 2):
        node = queue.pop(0)
        if vals[i] is not None:
            node.left = TreeNode(vals[i])
            queue.append(node.left)
        if i + 1 < len(vals) and vals[i + 1] is not None:
            node.right = TreeNode(vals[i + 1])
            queue.append(node.right)
    return head
    
