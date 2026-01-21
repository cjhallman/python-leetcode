import pytest

from leetcode_solutions.problem91.solution import Solution


@pytest.mark.parametrize(
    "s,expected",
    [("06", 0), ("12", 2), ("226", 3)],
)
def test_partition(s, expected):
    solution = Solution()
    assert solution.numDecodings(s) == expected
