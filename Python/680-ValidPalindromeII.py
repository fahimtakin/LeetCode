class Solution:
    def validPalindrome(self, s: str) -> bool:
        leftPtr, rightPtr = 0, len(s)-1 # set two pointers at two ends
        while(leftPtr < rightPtr):
            if s[leftPtr] != s[rightPtr]:
                skipL = s[leftPtr+1 : rightPtr + 1] # if two pointer values aren't same skip the values
                skipR = s[leftPtr : rightPtr]  # if two pointer values aren't same skip the values
                return (skipL == skipL[::-1] or skipR == skipR[::-1]) # check if the reversed array and the modified array are the same
            leftPtr, rightPtr = leftPtr + 1, rightPtr - 1 # if value at left and right pointers are equal, then shift left pointer right and right pointer left
      
        return True
