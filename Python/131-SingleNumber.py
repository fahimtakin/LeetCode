class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0  # rest of the even number of XOR terms = 0
        for n in nums:
            res = n ^ res  # n XOR 0 = n
        return res
