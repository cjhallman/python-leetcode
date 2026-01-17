from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Left & Right pointer
        left starts at 0 is pointing at the end of the resulting array
        Right starts at 1 is pointing at the value in original array being considered
        """
        left, right = 0, 1
        cur_added = 1
        while right < len(nums):
            if nums[right] == nums[left]:
                if cur_added < 2:
                    left += 1
                    nums[left] = nums[right]
                    cur_added += 1
            else:
                left += 1
                nums[left] = nums[right]
                cur_added = 1
            right += 1
        return left + 1
