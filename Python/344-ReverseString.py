class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        leftPtr, rightPtr = 0, len(s)-1 #two pointers at two ends of the string
        while leftPtr < rightPtr:
            s[leftPtr], s[rightPtr] = s[rightPtr], s[leftPtr] # swap the values
            leftPtr = leftPtr + 1 # increment left pointer
            rightPtr = rightPtr - 1  # decrement right pointer
