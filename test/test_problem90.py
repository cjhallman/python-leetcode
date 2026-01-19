import pytest

from leetcode_solutions.problem90.solution import Solution


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 2, 2], [[1, 2, 2], [1, 2], [1], [2, 2], [2], []]),
        ([0], [[0], []]),
    ],
)
def test_partition(nums, expected):
    solution = Solution()
    assert solution.subsetsWithDup(nums) == expected
