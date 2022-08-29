class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        candidate = 0
        counter = 0
        for val in nums:
            if counter == 0:
                candidate = val

            if candidate == val:  # if the same value increments
                counter += 1
            else:
                counter -= 1  # if different value decrements

        return candidate
