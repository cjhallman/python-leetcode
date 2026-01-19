import pytest

from leetcode_solutions.nodes.nodes import buildHeadFromList
from leetcode_solutions.problem86.solution import Solution


@pytest.mark.parametrize(
    "input, x, expected",
    [
        ([2, 1], 2, [1, 2]),
        ([1, 4, 3, 2, 5, 2], 3, [1, 2, 2, 4, 3, 5]),
        ([1, 4, 3, 2, 5, 2], 6, [1, 4, 3, 2, 5, 2]),
        ([1, 4, 3, 2, 5, 2], 0, [1, 4, 3, 2, 5, 2]),
        ([1], 2, [1]),
        ([1], 0, [1]),
        ([], 0, []),
    ],
)
def test_partition(input, x, expected):
    solution = Solution()
    head = buildHeadFromList(input)
    expected_head = buildHeadFromList(expected)
    assert solution.partition(head, x) == expected_head
