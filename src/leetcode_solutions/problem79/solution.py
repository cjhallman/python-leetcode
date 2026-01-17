from typing import List, Set


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        We can go through the list until we find the the starting letter
        Then start dfs from that spot
        """
        rows = len(board)
        cols = len(board[0])
        for row in range(rows):
            for col in range(cols):
                current_cell = board[row][col]
                if current_cell == word[0]:
                    if self.dfs((row, col), {(row, col)}, board, word[1:]):
                        return True
        return False

    def dfs(
        self,
        last_spot: tuple,
        current_path: Set[tuple],
        board: List[List[str]],
        word: str,
    ) -> bool:
        """
        BASE CASE: if word == "" -> True
        Look right, if not out of bounds, if next letter, not part of current path, try it
        Look down, if not out of bounds, if next letter, not part of current path, try it
        Look left, if not out of bounds, if next letter, not part of current path, try it
        Look up, if not out of bounds, if next letter, not part of current path, try it
        """
        if word == "":
            return True
        right_spot = (last_spot[0], last_spot[1] + 1)
        if self.trySpot(right_spot, current_path, board, word):
            return True
        down_spot = (last_spot[0] + 1, last_spot[1])
        if self.trySpot(down_spot, current_path, board, word):
            return True
        left_spot = (last_spot[0], last_spot[1] - 1)
        if self.trySpot(left_spot, current_path, board, word):
            return True
        up_spot = (last_spot[0] - 1, last_spot[1])
        if self.trySpot(up_spot, current_path, board, word):
            return True
        return False

    def isValidSpot(
        self, spot: tuple, current_path: Set[tuple], board: List[List[str]]
    ) -> bool:
        rows = len(board)
        cols = len(board[0])
        return (
            spot[0] < rows
            and spot[0] >= 0
            and spot[1] < cols
            and spot[1] >= 0
            and spot not in current_path
        )

    def spotIsNextLetter(self, spot: tuple, board: List[List[str]], word: str) -> bool:
        return board[spot[0]][spot[1]] == word[0]

    def trySpot(
        self, spot: bool, current_path: Set[tuple], board: List[List[str]], word: str
    ) -> bool:
        if self.isValidSpot(spot, current_path, board) and self.spotIsNextLetter(
            spot, board, word
        ):
            current_path.add(spot)
            if self.dfs(spot, current_path, board, word[1:]):
                return True
            current_path.remove(spot)
        return False
