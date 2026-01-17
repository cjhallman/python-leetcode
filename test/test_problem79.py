import pytest

from leetcode_solutions.problem79.solution import Solution


@pytest.mark.parametrize(
    "board, word, expected",
    [
        (
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            "ABCCED",
            True,
        ),
        (
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            "SEE",
            True,
        ),
        (
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            "ABCB",
            False,
        ),
    ],
)
def test_exist(board, word, expected):
    solution = Solution()
    assert solution.exist(board, word) == expected
