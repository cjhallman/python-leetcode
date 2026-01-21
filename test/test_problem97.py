import pytest

from leetcode_solutions.problem97.solution import Solution


@pytest.mark.parametrize(
    "s1,s2,s3,expected",
    [
        ("aabcc", "dbbca", "aadbbcbcac", True),
        ("aabcc", "dbbca", "aadbbbaccc", False),
        ("", "", "", True),
    ],
)
def test_partition(s1, s2, s3, expected):
    solution = Solution()
    assert solution.isInterleave(s1, s2, s3) == expected
