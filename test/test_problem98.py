from leetcode_solutions.nodes.nodes import buildTreeNodeFromList
import pytest

from leetcode_solutions.problem98.solution import Solution


@pytest.mark.parametrize(
    "nodes_as_list,expected",
    [
        ([2,1,3], True),
        ([5,1,4,None,None,3,6], False),
        ([2,2,2], False),
        ([[0,None,-1], False]),
        ([1,None,2,3], False),
        ([3, 9, 20, None, None, 15, 7], False)
    ],
)
def test_partition(nodes_as_list, expected):
    solution = Solution()
    root = buildTreeNodeFromList(nodes_as_list)
    assert solution.isValidBST(root) == expected
