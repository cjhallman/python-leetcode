class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        BFS - Just need to find the first interleaving that results in s3
        With each move, you can either take first char from s1 or s2
        Only want to take the char if it matches the next char of s3
        if s1 char matches -> explore s1 -> if works return true
        if s2 char matches -> explore s2 -> if works return true
        Else (neither char matches or both did not return true) -> invalid path -> backtrack
        """
        # Need to keep track of visited
        visited = set()

        def backtracking(i1: int, i2: int, i3: int):
            if (i1, i2, i3) in visited:
                # print(f"HIT: Already tried ({i1},{i2},{i3}) so we know it doesn't work")
                return False
            # print(f"backtracking({i1},{i2},{i3})")
            # BASE CASES
            # End of i1, i2, and i3 -> return True
            # leftover of s1 + leftover of s2 != leftover of s3 -> return False
            if i1 == len(s1) and i2 == len(s2) and i3 == len(s3):
                # print(f"VALID INTERLEAVE FOUND!")
                return True
            if (len(s1) - i1) + (len(s2) - i2) != (len(s3) - i3):
                return False
            # If current char of s1 == current char of s3 -> explore
            if i1 < len(s1) and i3 < len(s3) and s1[i1] == s3[i3]:
                # print(f"s1[{i1}] matches s3[{i3}] == {s3[i3]}")
                result = backtracking(i1 + 1, i2, i3 + 1)
                if result:
                    return True
            # If current char of s2 == current char of s3 -> explore
            if i2 < len(s2) and i3 < len(s3) and s2[i2] == s3[i3]:
                # print(f"s2[{i2}] matches s3[{i3}] == {s3[i3]}")
                result = backtracking(i1, i2 + 1, i3 + 1)
                if result:
                    return True
            # Else (neither char matches, no valid next step, both did not return true) -> invalid path -> backtrack
            visited.add((i1, i2, i3))
            return False

        return backtracking(0, 0, 0)
