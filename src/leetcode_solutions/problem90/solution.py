from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []
        nums.sort()

        def backtracking(i: int):
            print(f"backtracking({i})")
            if i == len(nums):
                print(f"Adding {subset} to result")
                result.append(subset[:])
                return

            subset.append(nums[i])
            print(f"generating all subsets that include {subset}")
            backtracking(i + 1)
            subset.pop()
            print(f"Backtracked {subset}")

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                print(f"Repeated int: {nums[i]}")
                i += 1

            backtracking(i + 1)

        backtracking(0)
        return result
