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
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            # print(f"l: {l}, r: {r}, mid: {mid}")

            if nums[mid] == target:
                return True

            if nums[mid] == nums[left] == nums[right]:
                # print(f"Can't figure out which side is sorted")
                left += 1
                right -= 1
                continue

            # Left Side sorted
            if nums[mid] >= nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # Right Side is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False
