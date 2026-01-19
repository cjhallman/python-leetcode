from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        """
        l, r = 0, len(nums) - 1
        mid = l + r // 2
        if nums[mid] == target -> return True
        if nums[mid] < target:
            if target < nums[r] -> Look to the right
            else -> Look to the left
        else (nums[mid] > target):
            if target > nums[l] -> Look to the left
            else -> look to the right
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            # print(f"l: {l}, r: {r}, mid: {mid}")

            if nums[mid] == target:
                return True

            if nums[mid] == nums[l] == nums[r]:
                # print(f"Can't figure out which side is sorted")
                l += 1
                r -= 1
                continue

            # Left Side sorted
            if nums[mid] >= nums[l]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
            # Right Side is sorted
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False
