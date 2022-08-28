class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        leftPtr, rightPtr = 0, len(nums) - 1
        # Binary Search
        while leftPtr <= rightPtr:
            mid = (leftPtr + rightPtr) // 2

            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                leftPtr = mid + 1
            else:
                rightPtr = mid - 1

        return leftPtr
