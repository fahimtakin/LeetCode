class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0  # left pointer starts at zero
        for r in range(len(nums)):  # right pointer goes through the array
            if nums[r] != 0:  # if right pointer number not equals to zero
                nums[r], nums[l] = nums[l], nums[r]  # then we exchange left and right pointer value
                l = l + 1  # increment left pointer

        return
