import pytest

from leetcode_solutions.problem80.solution import Solution


@pytest.mark.parametrize(
    "input, k, expected",
    [
        ([1, 1, 1, 2, 2, 3], 5, [1, 1, 2, 2, 3, 3]),
        ([0, 0, 1, 1, 1, 1, 2, 3, 3], 7, [0, 0, 1, 1, 2, 3, 3, 3, 3]),
        ([0], 1, [0]),
        ([0, 0], 2, [0, 0]),
    ],
)
def test_removeDuplicates(input, k, expected):
    solution = Solution()
    assert solution.removeDuplicates(input) == k
    assert input == expected
