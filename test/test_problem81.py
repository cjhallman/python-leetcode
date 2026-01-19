import pytest

from leetcode_solutions.problem81.solution import Solution


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([2,5,6,0,0,1,2], 0, True),
        ([2,5,6,0,0,1,2], 3, False),
        ([1,0,1,1,1], 0, True),
        ([1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1], 2, True),
        ([1,1,1,1,3,1], 3, True),
        ([3,5,1], 1, True),
        ([0,0,1,1,2,0], 2, True),
        ([1,2,0,1,1,1], 0, True),
    ],
)
def test_removeDuplicates(nums, target, expected):
    solution = Solution()
    assert solution.search(nums, target) == expected
