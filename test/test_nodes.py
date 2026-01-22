import pytest

from leetcode_solutions.nodes.nodes import buildListNodeFromList, ListNode, buildTreeNodeFromList, TreeNode

def test_ListNode():
    list_of_nodes = [1, 2, 3, 4, 5]
    list_node = buildListNodeFromList(list_of_nodes)
    assert list_node == ListNode(list_of_nodes[0],
                                  ListNode(list_of_nodes[1],
                                            ListNode(list_of_nodes[2],
                                                      ListNode(list_of_nodes[3],
                                                                ListNode(list_of_nodes[4], None)))))
    assert str(list_node) == "[1, 2, 3, 4, 5]"

def test_TreeNode():
    """
             1
              \
               2
              /
             3
    """
    list_of_nodes = [1, None, 2, 3]
    tree_node = buildTreeNodeFromList(list_of_nodes)
    head = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    assert tree_node == head
    assert str(head) == "[1, None, 2, 3]"
    assert str(tree_node) == "[1, None, 2, 3]"