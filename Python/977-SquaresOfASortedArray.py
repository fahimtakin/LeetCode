class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [] # empty array for storing results
        leftPtr, rightPtr = 0, len(nums)-1 # two pointers start from two ends
        
        while leftPtr <= rightPtr: 
            if nums[leftPtr] * nums[leftPtr] > nums[rightPtr] * nums[rightPtr]: # if square of left pointer value is greater
                res.append(nums[leftPtr] * nums[leftPtr])
                leftPtr += 1  # shift right
                
            else:
                res.append(nums[rightPtr] * nums[rightPtr])  # if square of right pointer value is greater or equal
                rightPtr -= 1 # shift left
                
        return res[::-1] # return the array in reversed order as the array is in descending order
