import pytest

from leetcode_solutions.nodes.nodes import buildHeadFromList
from leetcode_solutions.problem82.solution import Solution


@pytest.mark.parametrize(
    "input, expected",
    [
        ([1, 2, 3, 3, 4, 4, 5], [1, 2, 5]),
        ([1, 1, 1, 2, 3], [2, 3]),
        ([1, 2, 3, 3, 4, 4], [1, 2]),
        ([1], [1]),
        ([], []),
    ],
)
def test_deleteDuplicates(input, expected):
    solution = Solution()
    head = buildHeadFromList(input)
    expected_head = buildHeadFromList(expected)
    assert solution.deleteDuplicates(head) == expected_head
